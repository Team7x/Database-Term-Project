from flask import Flask,render_template,request,redirect,g,url_for,session

from flask_mysqldb import MySQL
from inventory import *

import os

app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        idp = request.form['IDP']
        nip = request.form['NIP']
        username = request.form['username']
        email = request.form['email']
        no_telp = request.form['no_telp']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO user (id,name,email) VALUES (%s,%s,%s)", (idp,username,email))
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pegawai (nip,id,no_telp) VALUES (%s,%s,%s)", (nip,idp,no_telp))
        mysql.connection.commit()

        cur.close()

        return "KITA TEMENAN AJA"
        
    return render_template('index.html')

@app.route('/tes')
def tes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from user where id='217504'")
    fetchdata=cur.fetchall()
    print(fetchdata)
    cur.close()

    return fetchdata[0][0]

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user',None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))

    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html',user=session['user'])

    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM user")
    
    if users > 0:
        userDetail = cur.fetchall()

        return render_template('users.html', userDetail=userDetail)

@app.route('/pegawai')
def pegawai():
    cur = mysql.connection.cursor()

    data = cur.execute("SELECT * FROM pegawai")

    if data >0:
        datadetail = cur.fetchall()

        return render_template('pegawai.html', datadetail=datadetail)