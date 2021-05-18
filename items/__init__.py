from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql6.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql6413208'
app.config['MYSQL_PASSWORD'] = 'Ekr5GmqjHP'
app.config['MYSQL_DB'] = 'sql6413208'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

from items import main