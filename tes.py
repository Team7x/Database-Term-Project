from flask import Flask,render_template,request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "testdoang"

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        idp = request.form['ID']
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

if __name__ == "__main__":
    app.run(debug=True)
