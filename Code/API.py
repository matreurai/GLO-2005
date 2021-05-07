GLO - 2005.
docx
Projet
GLO - 2005.
pdf
Projet
réel.pdf
test.py
#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------
import flask_mail
import mysql.connector
import json
import http.client
from flask import Flask ,render_template, redirect, url_for, request, session
from datetime import datetime
import bcrypt
from decimal import Decimal
from flask_mail import Mail
from threading import Timer
from BD_API.t_projet_import import *

# Init App
app = Flask(__name__)

alerts = []
hasModifiedAlert = False


#mail= Mail(app)
# Init Server
db = mysql.connector.connect(host="127.0.0.1", user="root", password="christopher", db="glo-2005-projet", auth_plugin='mysql_native_password')
app.secret_key = 'mucen3i2nmif3'
cur = db.cursor()


def update_data(interval):
  Timer(interval, update_data, [interval]).start()
  global hasModifiedAlert
  global alerts

  a = t_projet_live()

  if hasModifiedAlert == True:
    hasModifiedAlert = False
    alerts = select_all_alerts()

  if alerts:
    check_alerts(alerts)

#Route de la page home
@app.route('/')
def main():
  fetch_alerts()
  update_data(10)
  return render_template('Home.html')

#Route de la page home
@app.route('/Home')
def page_home():
  return render_template('Home.html')

#Route de la page contact
@app.route('/Contact')
def page_contact():
  return render_template('Contact.html')

#Route de la page about
@app.route('/About')
def page_about():
  return render_template('About.html')

#Route de la page Markets
@app.route('/Markets')
def page_markets():
  return render_template('Markets.html')

#Route de la page Portfolio
@app.route('/Portfolio')
def page_portfolio():
  data = get_all_crypto()
  get_portfolio_info()

  titreInfo = get_titre_info()
  titre_info_formatter = []

  paid_price_total = 0
  balance = 0
  if titreInfo:
    for i in titreInfo:
      ticker = get_crypto_ticker(i[0])[0]
      quantity = i[2]
      paid_price = round(i[3], 4)
      paid_price_total += round(paid_price * quantity, 4)
      #####
      ##### current_price = api...
      #####
      # A CHANGER 2142 POUR CURRENTPRICE
      profits_loss = round((quantity * 129) - (quantity * paid_price), 4)
      ratio = round(((quantity * 129) / (quantity * paid_price)), 4)
      balance += round(129 * quantity, 4)
      itemTitre = [ticker, 129, quantity, paid_price, profits_loss, ratio]
      titre_info_formatter.append(itemTitre)

  cmd = 'UPDATE t_portfolio SET portfolio_balance = %s, portfolio_cout_total = %s  WHERE portfolio_id = %s'
  cur = db.cursor()
  cur.execute(cmd, (balance, paid_price_total, session['portfolioId'], ))
  db.commit()


  data.append(titre_info_formatter)
  data.append(balance)

  return render_template('Portfolio.html', data=data)

#Route de la page Alerts
@app.route('/Alerts')
def page_alerts():
  data = get_all_crypto()

  data.append(get_alerts_info())

  return render_template('Alerts.html', data=data)

#Route de la page Profile
@app.route('/Profile')
def page_profile():
  data = get_user_info()

  return render_template('Profile.html', data=data)

@app.route('/LogOut')
def logout():
  user = session['username']
  session.pop(user, None)
  session.clear()
  return render_template('Home.html')

#Route de la page SignUp
@app.route('/SignUp')
def page_signup():
  return render_template('SignUp.html')

#Route du login
@app.route("/login_form", methods=['POST'])
def login():
  username = request.form.get('uname')
  password = request.form.get('psw')

  cmd='SELECT * FROM t_utilisateur u1 INNER JOIN t_password p1 on p1.password_id_utilisateur = u1.utilisateur_id WHERE u1.utilisateur_username = %s'
  cur=db.cursor()
  cur.execute(cmd,(username,))
  account = cur.fetchone()

  if account :
    cmd = 'SELECT p1.password_password FROM t_password p1 WHERE p1.password_id_utilisateur = %s'
    cur.execute(cmd, (account[0],))
    hash_password = cur.fetchone()

    if check_password(password, hash_password[0]):
      session['loggedin'] = True
      session['id'] = account[0]
      session['username'] = account[1]
      msg = 'Logged in successfully !'
    else:
      msg = 'Incorrect username / password'
  else:
    msg = 'Incorrect username / password'
  return render_template("home.html", msg=msg)

@app.route("/profile_form", methods=['POST'])
def savechanges_profile():
  username = request.form.get('username')
  password = request.form.get('password')
  email = request.form.get('email')
  firstname = request.form.get('firstname')
  lastname = request.form.get('lastname')
  phone = request.form.get('phone')

  userId = str(session['id'])
  cmd = 'SELECT utilisateur_id from t_utilisateur u1 WHERE u1.utilisateur_id = %s'
  cur = db.cursor()
  cur.execute(cmd, (userId,))
  data = cur.fetchone()
  idUser = data[0]

  cmd = 'UPDATE t_utilisateur SET utilisateur_username= %s, utilisateur_email= %s, utilisateur_phone= %s, utilisateur_prenom= %s, utilisateur_nom= %s WHERE utilisateur_id = %s'

  cur.execute(cmd, (username, email, phone, firstname, lastname, idUser,))

  cmd = 'UPDATE t_password SET password_password= %s WHERE password_id_utilisateur= %s'
  cur = db.cursor()
  cur.execute(cmd, (get_hashed_password(password), idUser,))
  db.commit()
  data = get_user_info()

  return render_template('Profile.html', data=data)

@app.route('/deletetitre', methods = ['POST'])
def deletetitre():
    info = request.form.getlist("javascript_data[]")
    portfolioId = int(session['portfolioId'])
    qte = int(info[2])
    prix = float(info[3][:-1])
    coin = info[0]

    result = get_crypto_id(coin)

    cmd = 'DELETE from t_titre u1 WHERE u1.titre_crypto_id LIKE %s AND u1.titre_portfolio_id LIKE %s AND u1.titre_qte LIKE %s  AND abs(u1.titre_prix_moyen_paye - %s) < 0.001'
    cur = db.cursor()
    cur.execute(cmd, (result[0], portfolioId, qte, prix,))
    db.commit()
    return redirect(url_for("page_portfolio"))


@app.route('/deletealert', methods = ['POST'])
def deletealert():
    info = request.form.getlist("javascript_data[]")
    userId = str(session['id'])
    ticker = info[0]
    below = info[1]
    above = info[2]
    endDate = datetime.strptime(info[3], '%Y-%m-%d').date()

    # rajouter AND u1.alerte_ticker LIKE %s quand la db sera rempli
    cmd = 'DELETE from t_alerte u1 WHERE u1.alerte_user = %s AND u1.alerte_below_price = CAST(%s AS DECIMAL) ' \
          'AND u1.alerte_above_price = CAST(%s AS DECIMAL) AND u1.alerte_end_date = %s'
    cur = db.cursor()
    cur.execute(cmd, (userId, below, above, endDate,))
    db.commit()
    global hasModifiedAlert
    hasModifiedAlert = True
    return redirect(url_for("page_alerts"))


@app.route("/portfolio_form", methods=['POST'])
def apply_portfolio():
  coin = request.form.get('coin')
  paidprice = float(request.form.get('paidprice'))
  quantity = float(request.form.get('quantity'))
  userId = str(session['id'])

  cmd = 'SELECT u1.portfolio_id FROM t_portfolio u1 WHERE u1.portfolio_user = %s'
  cur = db.cursor()
  cur.execute(cmd, (userId,))
  portfolio_id = cur.fetchone()

  crypto_id = get_crypto_id(coin)

  cmd = 'INSERT INTO t_titre (titre_crypto_id, titre_portfolio_id, titre_qte, titre_prix_moyen_paye) VALUES (%s,%s,%s,%s)'
  cur = db.cursor()
  cur.execute(cmd, (crypto_id[0], portfolio_id[0], quantity, paidprice,))
  db.commit()

  return redirect(url_for("page_portfolio"))

@app.route("/alerts_form", methods=['POST'])
def apply_alerts():
  coin = request.form.get('coin')
  above = float(request.form.get('above'))
  below = float(request.form.get('below'))
  validUntil = datetime.strptime(request.form.get('datepicker'), '%Y-%m-%d').date()
  userId = str(session['id'])

  crypto_id = get_crypto_id(coin)

  cmd = 'SELECT * FROM t_alerte u1 WHERE u1.alerte_user = %s AND u1.alerte_below_price = CAST(%s AS DECIMAL) ' \
          'AND u1.alerte_above_price = CAST(%s AS DECIMAL) AND u1.alerte_end_date = %s AND u1.alerte_ticker = %s '
  cur = db.cursor()
  cur.execute(cmd, (userId, below, above, validUntil, crypto_id[0],))
  existingAlert = cur.fetchone()

  if existingAlert == None:
    cmd = 'INSERT INTO t_alerte (alerte_user, alerte_below_price, alerte_above_price, alerte_end_date, alerte_ticker) VALUES (%s,%s,%s,%s,%s)'
    cur = db.cursor()
    cur.execute(cmd, (userId, below, above, validUntil, coin,))
    db.commit()
    global hasModifiedAlert
    hasModifiedAlert = True

  return redirect(url_for("page_alerts"))

#Route du sign up
@app.route("/signup_form", methods=['POST'])
def signup():
  username = request.form.get('username')
  password = request.form.get('password')
  email = request.form.get('email')

  cmd = 'SELECT u1.utilisateur_username FROM t_utilisateur u1 WHERE u1.utilisateur_username = %s OR u1.utilisateur_email = %s'
  cur = db.cursor()
  cur.execute(cmd, (username, email,))
  userExist = cur.fetchone()

  if userExist is not None:
    return render_template('Home.html')

  hashedpwd = get_hashed_password(password)

  idUser = ""

  cur=db.cursor()
  args = [username, email, datetime.today().strftime("%Y-%m-%d"), hashedpwd, idUser]

  user = cur.callproc('Create_User', args)

  cmd = 'SELECT u1.portfolio_id FROM t_portfolio u1 WHERE u1.portfolio_user = %s'
  cur = db.cursor()
  cur.execute(cmd, (user[4],))
  portfolioId = cur.fetchone()

  session['portfolioId'] = portfolioId[0]

  cur.close()

  db.commit()


  return render_template('Home.html')

def get_user_info():
  userId = str(session['id'])
  cmd = 'SELECT * from t_utilisateur u1 WHERE u1.utilisateur_id = ' + userId + ''
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchone()

def get_portfolio_info():
  userId = str(session['id'])
  cmd = 'SELECT * from t_portfolio u1 WHERE u1.portfolio_user = ' + userId + ''
  cur = db.cursor()
  cur.execute(cmd)
  result = cur.fetchall()
  session['portfolioId'] = result[0][0]
  return result

def get_titre_info():
  portfolioId = str(session['portfolioId'])
  cmd = 'SELECT * from t_titre u1 WHERE u1.titre_portfolio_id = ' + portfolioId + ''
  cur = db.cursor()
  cur.execute(cmd)
  result = cur.fetchall()
  #Rajouter la logique des profits, balance, etc...
  #result.append()

  return result

def get_all_crypto():
  cmd = 'SELECT u1.cryptomonnaie_ticker from t_cryptomonnaie u1'
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchall()

def get_alerts_info():
  userId = str(session['id'])
  cmd = 'SELECT * from t_alerte u1 WHERE u1.alerte_user = ' + userId + ''
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchall()

def get_crypto_ticker(coin_id):
  cmd = 'SELECT cryptomonnaie_ticker from t_cryptomonnaie u1 WHERE u1.cryptomonnaie_id = %s'
  cur = db.cursor()
  cur.execute(cmd, (coin_id,))
  return cur.fetchone()

def get_crypto_id(coin):
  cmd = 'SELECT cryptomonnaie_id from t_cryptomonnaie u1 WHERE u1.cryptomonnaie_ticker = %s'
  cur = db.cursor()
  cur.execute(cmd, (coin,))
  return cur.fetchone()

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
  # Check hashed password. Using bcrypt, the salt is saved into the hash itself
  return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))


def check_alerts(alerts):
  for item in alerts:
    alerteId = item[0]
    UserId = item[1]
    ticker = item[2]
    below = item[3]
    above = item[4]
    endDate = item[5]
    today = datetime.date(datetime.today())

    if endDate < today:
      delete_alert(alerteId)

    #Logique du below et above avec le ticker
    #if current price < below:
    # send email


def fetch_alerts():
  global alerts
  alerts = select_all_alerts()


def delete_alert(alerteId):
  cmd = 'DELETE from t_alerte u1 WHERE u1.alerte_id = %s'
  cur = db.cursor()
  cur.execute(cmd, (alerteId,))
  db.commit()
  global hasModifiedAlert
  hasModifiedAlert = True


def select_all_alerts():
  cmd = 'SELECT * FROM t_alerte u1'
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchall()

def send_email(type, price):
  SERVER = "smtp.live.com"
  FROM = "cryptowatch@hotmail.com"

  cmd = 'SELECT utilisateur_email from t_utilisateur u1 WHERE u1.utilisateur_username = %s'
  cur = db.cursor()
  cur.execute(cmd, (session['username'],))
  userMail = cur.fetchone()

  TO = [userMail[0]]  # must be a list

  SUBJECT = "Crypt-O-Watch | Alert - {coin} is now {below ou above} {price}!"
  TEXT = "Crypt-O-Watch Watch out! {coin} is now {below ou above} {price}! Thanks! Be Your Own Bank"

  # Prepare actual message
  message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

  %s
  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

  # Send the mail
  import smtplib
  server = smtplib.SMTP(SERVER, 587)
  server.starttls()
  server.login(FROM, "Sam1David2Christopher3")
  server.sendmail(FROM, TO, message)
  server.quit()

def mise_a_jour():
      return None


if __name__ == '__main__':
  app.run(debug=True)


def exchange_dict ():
  conn = http.client.HTTPSConnection("api.binance.com")
  payload = ''
  headers = {
    'Content-Type': 'application/json'
  }
  conn.request("GET", "/api/v3/exchangeInfo", payload, headers)
  res = conn.getresponse()
  data = res.read()
  transfor = data.decode("utf-8")
  exchange_dict = json.loads(transfor)
  print (type(exchange_dict['symbols']))
  
  for stocks in exchange_dict['symbols']:
    return (stocks['symbol'])

#Call cette fonction de la méthode page_home() SEULEMENT si on veut hash tous les passwords de la DB (si c'est pas déjà fait)
def hash_allpasswords():
  cmd = 'SELECT * FROM t_password'
  cur = db.cursor()
  cur.execute(cmd)
  info = cur.fetchall()
  for i in info:
    password = i[1]
    hash_pass = get_hashed_password(password)
    cmd = 'UPDATE t_password SET password_password=\'' + hash_pass + '\' WHERE password_id_utilisateur=\'' + str(
      i[0]) + '\';'
    cur = db.cursor()
    cur.execute(cmd)
    db.commit()