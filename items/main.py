from flask import Flask,render_template,request,redirect,g,url_for,session
from flask_mysqldb import MySQL
from items import *

import os

app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        a = request.form['resi']
        b = request.form['namapengirim']
        c = request.form['namapenerima']
        d = request.form['notelppengirim']
        e = request.form['notelppenerima']
        f = request.form['alamatpenerima']
        g = request.form['beratbarang']
        h = request.form['tgl']
        i = request.form['harga']
        j = request.form['nip']
        k = request.form['id_kota']
        l = request.form['id_status']
        m = request.form['estimasi']

        cur = mysql.connection.cursor()

        cur.execute("""INSERT INTO order2 (resi,namaPengirim,namaPenerima,no_telp_pengirim,
        no_telp_penerima,alamat_penerima,beratBarang,tgl_pengiriman,hargaTotal,nip,id_kota,id_status,estimasi) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (a,b,c,d,e,f,g,h,i,j,k,l,m))
        mysql.connection.commit()

        cur.close()

        return "loh loh loh"
        
    return render_template('index.html')