from flask import Flask,render_template,request,redirect,g,url_for,session
from flask_mysqldb import MySQL
from items import *
from items.user import *
import datetime

import os

app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def login():
    global loguser

    if request.method == 'POST':
        userid = request.form['nim']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('select * from admin')
        admin = cur.fetchall()

        for i in range(len(admin)):
            if str(admin[i][3]) == str(password):
                print(admin[i][3])
                print(password)
                loguser = user(admin[i][0],admin[i][1],admin[i][2])
                print(loguser)
                return redirect(url_for('menu'))
        

    return render_template('index.html')


@app.route('/menu',methods=['GET','POST'])
def menu():
    if loguser.nim() == "":
        return "blm login"

    else:
        return render_template('menu.html')


# INPUT 

@app.route('/input/order',methods=['GET','POST'])
def inputorder():
    
    if request.method == 'POST':
        a = request.form['resi']
        b = request.form['namapengirim']
        c = request.form['namapenerima']
        d = request.form['notelppengirim']
        e = request.form['notelppenerima']
        f = request.form['alamatpenerima']
        g = request.form['beratbarang']
        j = request.form['nip']
        k = request.form['id_kota']

        cur = mysql.connection.cursor()
        cur.execute(f"select id_tipe from kurir where nip='{j}'")
        idtipe= cur.fetchall()
        idtipe= idtipe[0][0]

        cur.execute(f"select hargaTipe,lama from tipe where id_tipe='{idtipe}'")
        hargaTipeLama = cur.fetchall()

        hargaTipe = hargaTipeLama[0][0]
        lama= hargaTipeLama[0][1]
        hargaTipe = float(hargaTipe)/2

        cur.execute(f"select hargaKota from kota where id_kota='{k}'")
        KotaLama = cur.fetchall()
        Kota=KotaLama[0][0]

        hargaTipe = hargaTipe * int(g) * int(Kota)


        x = datetime.datetime.now()
        tgl = (f'{x.year}-{x.month}-{int(x.day)+lama}')
        print(tgl)

        cur.close()
        cur = mysql.connection.cursor()

        cur.execute("""INSERT INTO order2 (resi,namaPengirim,namaPenerima,no_telp_pengirim,
        no_telp_penerima,alamat_penerima,beratBarang,tgl_pengiriman,hargaTotal,nip,id_kota,id_status,estimasi) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (a,b,c,d,e,f,g,datetime.date.today(),hargaTipe,j,k,'0',tgl))
        mysql.connection.commit()

        cur.close()

        return "loh loh loh"
        
    return render_template('/input/order.html')

@app.route('/input/kurir',methods=['GET', 'POST'])
def inputkurir():

    if request.method == "POST":
        a = request.form['nip']
        b = request.form['nama']
        c = request.form['tgl_masuk']
        d = request.form['alamat']
        e = request.form['notel']
        g = request.form['id_tipe']

        today = datetime.datetime.today()
        someday = datetime.datetime.strptime(c, "%Y-%m-%d")
        cal = today - someday
        f = cal.days
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)

        cur = mysql.connection.commit()
        cur.execute(f"insert into kurir values ('{a}','{b}','{c}','{d}','{e}','{f}','{g}')")
        cur.connection.commit()
        cur.close()

        return "BERHASIL MENAMBAH KURIR!"
    
    return render_template('/input/kurir.html')

@app.route('/input/kota',methods=['GET','POST'])
def inputkota():

    if request.method == "POST":
        a = request.form['id_kota']
        b = request.form['namakota']
        c = request.form['hargakota']

        cur = mysql.connection.commit()
        cur.execute(f"insert into kota values ('{a}','{b}','{c}')")
        cur.connection.commit()
        cur.close()

    return render_template('/input/kota.html')


#SHOW

@app.route('/show',methods=['POST','GET'])
def show():
    
    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('show.html')
    else:
        return render_template('show.html')
    

@app.route('/show/kota',methods=['POST','GET'])
def showkota():
    
    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('/show/kota.html')
    else:
        cur = mysql.connection.cursor()
        cur.execute(f'select * from kota')
        kota = cur.fetchall()
        cur.close()

        return render_template('/show/kota.html', kota=kota)

@app.route('/show/order',methods=['POST','GET'])
def showorder():
    
    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('/show/order.html')
    else:
        cur = mysql.connection.cursor()
        cur.execute(f'select * from order2')
        order2 = cur.fetchall()
        cur.close()

        return render_template('/show/order.html',order2=order2)


@app.route('/show/kurir',methods=['POST','GET'])
def showkurir():
    
    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('/show/kurir.html')
    else:
        cur = mysql.connection.cursor()
        cur.execute(f'select * from kurir')
        kurir = cur.fetchall()
        cur.close()
        return render_template('/show/kurir.html',kurir=kurir)
