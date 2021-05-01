#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------
import mysql.connector
import json
import http.client
from flask import Flask ,render_template, request, session
from datetime import date
import bcrypt

# Init App
app = Flask(__name__)
# Init Server
db = mysql.connector.connect(host="127.0.0.1", user="root", password="password", db="glo-2005-projet", auth_plugin='mysql_native_password')
app.secret_key = 'mucen3i2nmif3'
# Def du cursor
cur = db.cursor()

#Route de la page home
@app.route('/')
def main():
  return render_template('Home.html')
# time stamp

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
  return render_template('Portfolio.html')

#Route de la page Alerts
@app.route('/Alerts')
def page_alerts():
  data = get_alerts_info()
  data = ['a','v']

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

@app.route("/alerts_form", methods=['POST'])
def apply_alerts():
  coin = request.form.get('coin')
  above =request.form.get('above')
  below = request.form.get('below')
  validUntil = request.form.get('valid_until')
  userId = str(session['id'])

  cmd = 'INSERT INTO t_alerte (alerte_user, alerte_ticker, alerte_below_price, alerte_above_price, alerte_end_date) VALUES (%s,%s,%s,%s,%s)'
  cur = db.cursor()
  cur.execute(cmd, (userId, coin, below, above, validUntil,))
  db.commit()
  data = get_alerts_info()

  return render_template('Alerts.html', data=data)

#Route du sign up
@app.route("/signup_form", methods=['POST'])
def signup():
  username = request.form.get('username')
  password = request.form.get('password')
  email = request.form.get('email')

  hashedpwd = get_hashed_password(password)

  cur=db.cursor()
  args = [username, email, date.today().strftime("%Y-%m-%d"), hashedpwd]

  cur.callproc('Create_User', args)
  cur.close()

  cur = db.cursor()
  db.commit()
  return render_template('Home.html')

def get_user_info():
  userId = str(session['id'])
  cmd = 'SELECT * from t_utilisateur u1 WHERE u1.utilisateur_id = ' + userId + ''
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchone()

def get_alerts_info():
  userId = str(session['id'])
  cmd = 'SELECT * from t_alerte u1 WHERE u1.alerte_id = ' + userId + ''
  cur = db.cursor()
  cur.execute(cmd)
  return cur.fetchall()

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
  # Check hashed password. Using bcrypt, the salt is saved into the hash itself
  return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))

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