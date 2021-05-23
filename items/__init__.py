from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ekspedisi'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

from items import main