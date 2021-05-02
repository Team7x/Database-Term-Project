from flask import Flask,render_template,request

from flask_mysqldb import MySQL

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "ekspedisi"

mysql = MySQL(app)

from items import main