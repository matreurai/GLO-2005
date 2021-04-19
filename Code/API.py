#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------
import mysql.connector
import json
import http.client
from flask import Flask ,render_template , request
import MySQLdb
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

# Init App
app = Flask(__name__)
# Init Server
db = MySQLdb.connect("localhost","root","christopher","glo-2005-projet")

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
  courriel = request.form.get('uname')
  passe = request.form.get('psw')
  conn = mysql.connector.connect(host='localhost',
                                 database='glo-2005-projet',
                                 user='root',
                                 password='christopher')
  cmd='SELECT utilisateur_password FROM t_utilisateur WHERE utilisateur_username='+courriel+';'
  cur=conn.cursor()
  cur.execute(cmd)
  passeVrai = cur.fetchone()
  if (passeVrai!=None) and (passe==passeVrai[0]):
    cmd='SELECT * FROM utilisateurs WHERE courriel='+courriel+';'
    cur=conn.cursor()
    cur.execute(cmd)
    info = cur.fetchone()
    global ProfileUtilisateur
    ProfileUtilisateur["courriel"]=courriel
    ProfileUtilisateur["nom"]=info[2]
    ProfileUtilisateur["avatar"]=info[3]
    return render_template('bienvenu.html', profile=ProfileUtilisateur)
  return render_template('login.html', message="Informations invalides!")

#Route du sign up
@app.route("/signup_form", methods=['POST'])
def signup():
  username = request.form.get('username')
  password = request.form.get('password')
  email = request.form.get('email')
  conn = mysql.connector.connect(host='localhost',
                                 database='glo-2005-projet',
                                 user='root',
                                 password='christopher')
  cmd='INSERT INTO t_utilisateur (utilisateur_username, utilisateur_password, utilisateur_email, utilisateur_date_creation) ' \
      'VALUES(\''+username+'\', \''+password+'\', \''+email+'\', \''+date.today().strftime("%Y-%m-%d")+'\');'
  cur=conn.cursor()
  cur.execute(cmd)
  conn.commit()
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
    conn = mysql.connector.connect(host='localhost',
                                   database='glo-2005-projet',
                                   user='root',
                                   password='christopher')

    cmd = 'SELECT * FROM t_utilisateur'
    cur = conn.cursor()
    cur.execute(cmd)
    info = cur.fetchall()
    for i in info:
      password = i[2]
      hash_pass = generate_password_hash(password)
      cmd = 'UPDATE t_utilisateur SET utilisateur_password=\'' + hash_pass + '\' WHERE utilisateur_id=\'' + str(
        i[0]) + '\';'
      cur = conn.cursor()
      cur.execute(cmd)
      conn.commit()