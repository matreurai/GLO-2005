#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------
import mysql.connector
import json
import http.client
from flask import Flask ,render_template, request, session
import MySQLdb
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

# Init App
app = Flask(__name__)
# Init Server
db = MySQLdb.connect("localhost","root","christopher","glo-2005-projet")
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
  return render_template('Alerts.html')

#Route de la page Profile
@app.route('/Profile')
def page_profile():
  return render_template('Profile.html')

#Route de la page SignUp
@app.route('/SignUp')
def page_signup():
  return render_template('SignUp.html')

#Route du login
@app.route("/login_form", methods=['POST'])
def login():
  username = request.form.get('uname')
  password = hashlib.md5((request.form.get('psw')).encode('utf-8')).hexdigest()
  cmd='SELECT * FROM t_utilisateur WHERE utilisateur_username = %s AND utilisateur_password = %s'
  cur=db.cursor()
  cur.execute(cmd,(username,password,))
  account = cur.fetchone()

  if account:
    session['loggedin'] = True
    session['id'] = account[0]
    session['username'] = account[1]
    msg = 'Logged in successfully !'
  else:
    msg = 'Incorrect username / password'
  return render_template("home.html", msg=msg)

#Route du sign up
@app.route("/signup_form", methods=['POST'])
def signup():
  username = request.form.get('username')
  password = request.form.get('password')
  email = request.form.get('email')

  cmd=('INSERT INTO t_utilisateur (utilisateur_username, utilisateur_password, utilisateur_email, utilisateur_date_creation) ' \
      'VALUES(%s,%s,%s,%s)')
  cur=db.cursor()
  cur.execute(cmd, (username, hashlib.md5(password.encode('utf-8')).hexdigest(), email, date.today().strftime("%Y-%m-%d"),))
  db.commit()
  return render_template('Home.html')


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
  cmd = 'SELECT * FROM t_utilisateur'
  cur = db.cursor()
  cur.execute(cmd)
  info = cur.fetchall()
  for i in info:
    password = i[2]
    hash_pass = generate_password_hash(password)
    cmd = 'UPDATE t_utilisateur SET utilisateur_password=\'' + hash_pass + '\' WHERE utilisateur_id=\'' + str(
      i[0]) + '\';'
    cur = db.cursor()
    cur.execute(cmd)
    db.commit()