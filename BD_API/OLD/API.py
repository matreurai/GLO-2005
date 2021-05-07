# -------------------------------
# Test API Binance
# David Bolduc
# -------------------------------


import pymysql.cursors
from flask import Flask

# Init App
app = Flask(__name__)
# Init Server
db = pymysql.connect(host="localhost", user="root", password="christopher", db="GLO-2005-Projet")

# Def du cursor
cur = db.cursor()

requete='select * from '

# Route de la page home
@app.route('/Home')
# time stamp

def mise_a_jour():
    return None


if __name__ == '__main__':
    app.run(debug=True)
