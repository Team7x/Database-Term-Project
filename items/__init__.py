from flask import Flask,render_template,request

from flask_mysqldb import MySQL

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['MYSQL_HOST'] = 'sql6.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql6410548'
app.config['MYSQL_PASSWORD'] = 'n9jqhnGTCP'
app.config['MYSQL_DB'] = 'sql6410548'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

from items import main