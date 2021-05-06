from flask import Flask,render_template,request,redirect,g,url_for,session
from flask_mysqldb import MySQL
from items import *
from items.user import *
import datetime
import matplotlib.pyplot as plt


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
            if (str(admin[i][0]) == str(userid)) and (str(admin[i][3]) == str(password)):

                loguser = user(admin[i][0],admin[i][1],admin[i][2])
                print(loguser.__dict__)
                return redirect(url_for('menu'))
        

    return render_template('index.html')


@app.route('/menu',methods=['GET','POST'])
def menu():
    try:
        if loguser.nim() == "":
            return "blm login"

        else:
            return render_template('menu.html')
    except:
        return redirect('/')


# INPUT 

@app.route('/input/order',methods=['GET','POST'])
def inputorder():
    cur = mysql.connection.cursor()
    cur.execute(f"select * from kota")
    dataKota = cur.fetchall()
    cur.execute(f"select * from kurir")
    dataKurir = cur.fetchall()
    detailKurir = {
        "idkurir" : [],
        "nama" : [],
        "tipe" : []
    }
    for i in dataKurir:
        cur = mysql.connection.cursor()
        cur.execute(f"select namaTipe from tipe where id_tipe={i[5]}")
        temp = cur.fetchall()
        detailKurir["tipe"].append(temp[0][0])
        detailKurir["idkurir"].append(i[0])
        detailKurir["nama"].append(i[1])
        cur.close()
    
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

        return redirect('/show/order')
        
    return render_template('/input/order.html', dataKota=dataKota, dataKurir=dataKurir, detailKurir=detailKurir)

@app.route('/input/kurir',methods=['GET', 'POST'])
def inputkurir():
    cur = mysql.connection.cursor()
    cur.execute(f"select * from tipe")
    dataTipe = cur.fetchall()
    cur.close()
    if request.method == "POST":
        a = request.form['nip']
        b = request.form['nama']
        c = request.form['tgl_masuk']
        d = request.form['alamat']
        e = request.form['notel']
        g = request.form['id_tipe']


        cur = mysql.connection.cursor()
        cur.execute(f"insert into kurir values ('{a}','{b}','{c}','{d}','{e}','{g}')")
        cur.connection.commit()
        cur.close()

        return redirect('/show/kurir')
    
    return render_template('/input/kurir.html', dataTipe=dataTipe)

@app.route('/input/kota',methods=['GET','POST'])
def inputkota():

    if request.method == "POST":
        a = request.form['id_kota']
        b = request.form['namakota']
        c = request.form['hargakota']

        cur = mysql.connection.cursor()
        cur.execute(f"insert into kota values ('{a}','{b}','{c}')")
        cur.connection.commit()
        cur.close()

        return redirect('/show/kota')

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
        banyakOrder = []
        for i in kota:
            cur.execute(f'select count(resi) from order2 where id_kota={i[0]}')
            temp = cur.fetchall()
            banyakOrder.append(temp[0][0])
        cur.close()
        return render_template('/show/kota.html',kota=kota, banyakOrder=banyakOrder)

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

@app.route('/show/tipe',methods=['POST','GET'])
def showtipe():

    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('/show/tipe.html')
    else:

        cur = mysql.connection.cursor()
        cur.execute(f'select * from kurir')
        kurir = cur.fetchall()
        banyakOrder = []
        for i in kurir:
            cur.execute(f'select count(resi) from order2 where nip={i[0]}')
            temp = cur.fetchall()
            banyakOrder.append(temp[0][0])
        banyakOrder2 = []
        cur.execute(f'select * from tipe')
        tipe= cur.fetchall()
        for i in tipe:
            banyaktemp = 0
            for j in range(0, len(kurir)):
                if(i[0]==kurir[j][5]):
                    banyaktemp += banyakOrder[j]
            banyakOrder2.append(banyaktemp)
        cur.close()

        return render_template('/show/tipe.html',tipe=tipe, banyakOrder=banyakOrder2)
    

@app.route('/show/tipe/detail/<int:id>',methods=['POST','GET'])
def showtipekurir(id):

    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('/show/tipe.html')
    else:

        cur = mysql.connection.cursor()
        cur.execute(f"select * from kurir where id_tipe='{id}'")
        kurir= cur.fetchall()
        banyakOrder = []
        for i in kurir:
            cur.execute(f'select count(resi) from order2 where nip={i[0]}')
            temp = cur.fetchall()
            banyakOrder.append(temp[0][0])
        cur.close()

        return render_template('/show/tipe/detail.html',kurir=kurir, banyakOrder=banyakOrder)    


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
        banyakOrder = []
        for i in kurir:
            cur.execute(f'select count(resi) from order2 where nip={i[0]}')
            temp = cur.fetchall()
            banyakOrder.append(temp[0][0])
        cur.close()
        return render_template('/show/kurir.html',kurir=kurir, banyakOrder=banyakOrder)

@app.route('/editOrder/<int:id>')
def editOrder(id):
    #try:
    cur = mysql.connection.cursor()
    cur.execute(f"""SELECT order2.*, namaKurir, no_telp_Kurir, namaKota, hargaKota,
    namaTipe, hargaTipe
    FROM order2 NATURAL JOIN kurir NATURAL JOIN tipe NATURAL JOIN kota where resi='{id}'
    """)
    kurirDetail = cur.fetchall()
    cur.close()
    return render_template('/edit/order.html', kurirDetail=kurirDetail)
    #except:
    return "ada yang salah"

@app.route('/delO/<int:id>')
def delOrder(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f'DELETE FROM order2 WHERE resi={id}')
        cur.connection.commit()
        cur.close()
        return redirect('/show/order')
    except:
        return "ada yang salah"


@app.route('/delKota/<int:id>')
def delKota(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f'DELETE FROM kota WHERE id_kota={id}')
        cur.connection.commit()
        cur.close()
        return redirect('/show/kota')
    except:
        return "gagal apus"

@app.route('/delKurir/<int:id>')
def delKurir(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f'DELETE FROM kurir WHERE nip={id}')
        cur.connection.commit()
        cur.close()
        return redirect('/show/kurir')
    except:
        return "gagal hapus, kurir masi bawa barang"


@app.route('/delTipe/<int:id>')
def delTipe(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(f'DELETE FROM tipe WHERE id_tipe={id}')
        cur.connection.commit()
        cur.close()
        return redirect('/show/tipe')
    except:
        return "ada yang salah"

@app.route('/show/graphic',methods=['POST','GET'])
def showgraph():
    
    if request.method == "POST":
        if loguser.nim() == "":
            return "login duls"
        else:
            return render_template('show/graphic.html')
    else:
        return render_template('show/graphic.html')

@app.route('/show/graphic/kota')
def grapkota():
    cur = mysql.connection.cursor()
    cur.execute(f'select * from kota')
    kota = cur.fetchall()
    banyakOrder = []
    for i in kota:
        cur.execute(f'select count(resi) from order2 where id_kota={i[0]}')
        temp = cur.fetchall()
        banyakOrder.append(temp[0][0])

    cur.execute('select namaKota from kota')
    basing = cur.fetchall()
    
    graphkota=[]

    for i in basing:
        graphkota.append(i[0])

    print(graphkota)
    print(banyakOrder)
    fig = plt.figure(figsize=(7,5))
    plt.bar(graphkota,banyakOrder,width=0.5)

    plt.savefig('items/static/kotapic.png')
    image_file = url_for('static', filename='kotapic.png')
    return render_template('show/graphic/kota.html', graphkota_pic=image_file)

@app.route('/show/graphic/kurir')
def grapkurir():

    cur = mysql.connection.cursor()
    cur.execute(f'select * from kurir')
    kurir = cur.fetchall()
    banyakOrder = []
    for i in kurir:
        cur.execute(f'select count(resi) from order2 where nip={i[0]}')
        temp = cur.fetchall()
        banyakOrder.append(temp[0][0])

    cur.execute('select namaKurir from kurir')
    basing = cur.fetchall()
    
    graphkurir=[]

    for i in basing:
        graphkurir.append(i[0])

    print(graphkurir)
    print(banyakOrder)
    fig = plt.figure(figsize=(7,5))
    plt.bar(graphkurir,banyakOrder,width=0.5)

    plt.savefig('items/static/kurirpic.png')
    image_file = url_for('static', filename='kurirpic.png')
    
    return render_template('show/graphic/kurir.html', graphkurir_pic=image_file)


@app.route('/show/graphic/tipe')
def graptipe():
    cur = mysql.connection.cursor()
    cur.execute(f'select * from kurir')
    kurir = cur.fetchall()
    banyakOrder = []
    for i in kurir:
        cur.execute(f'select count(resi) from order2 where nip={i[0]}')
        temp = cur.fetchall()
        banyakOrder.append(temp[0][0])
    banyakOrder2 = []
    cur.execute(f'select * from tipe')
    tipe= cur.fetchall()
    for i in tipe:
        banyaktemp = 0
        for j in range(0, len(kurir)):
            if(i[0]==kurir[j][5]):
                banyaktemp += banyakOrder[j]
        banyakOrder2.append(banyaktemp)

    cur.execute('select namaTipe from tipe')
    basing = cur.fetchall()
    
    graphtipe=[]

    for i in basing:
        graphtipe.append(i[0])

    print(graphtipe)
    print(banyakOrder2)

    fig = plt.figure(figsize=(7,5))
    plt.bar(graphtipe,banyakOrder2,width=0.5)

    plt.savefig('items/static/tipepic.png')
    image_file = url_for('static', filename='tipepic.png')
    return render_template('show/graphic/tipe.html', graphtipe_pic=image_file)