
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =  'Arp123@'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'food'
mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def first():
    print("bye")
    if request.method == 'POST':
        # Fetch form data
            print("bye")
            userDetails = request.form
            uname = userDetails['uname']  
            email = userDetails['email']
            contact = userDetails['cont']
            password = userDetails['pass']
            cur = mysql.connection.cursor()
            query="Select *from sign where name=%s"
            cur.execute(query,(uname,))
            data=cur.fetchall()
            print(data)
            if(data==()):
                cur.execute("INSERT INTO sign(name,email,contact,password) VALUES(%s, %s,%s, %s)",(uname, email, contact, password))
                print("added")
                mysql.connection.commit()
                query="Select image from sign where name=%s"
                cur.execute(query,(uname,))
                data1=cur.fetchone()
                return render_template('home.html')
            else:
                return("username exits") 
    return render_template('main.html')




@app.route('/login', methods=['GET','POST'])
def log():
      if request.method == 'POST':
        # Fetch form data
        print("bye")
        userDetails = request.form
        email = userDetails['email']
        password = userDetails['pass']
        cur = mysql.connection.cursor()
        query="Select *from sign where email=%s and password=%s"
        cur.execute(query,(email,password,))
        data=cur.fetchall()
        print(data)
        if(data==()):
            return("please create account")
        else:     
             return render_template('home.html')
      return render_template('login.html')



@app.route('/adres', methods=['GET','POST'])
def adres():
    print("bye")
    if request.method == 'POST':
        # Fetch form data
            print("bye")
            userDetails = request.form
            uname = userDetails['uname']  
            password = userDetails['pass']
            r_name = userDetails['r_name']
            email = userDetails['email']
            add = userDetails['add']
            contact = userDetails['cont']
            spec = userDetails['food']
            lat = userDetails['lat']
            long = userDetails['long']
            cur = mysql.connection.cursor()
            query="Select *from sign where name=%s"
            cur.execute(query,(uname,))
            data=cur.fetchall()
            print(data)
            if(data==()):
                cur.execute("INSERT INTO restaurant(name,password,r_name,email,Address,cont,speciality,lat,longitutde) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s)",(uname, password,r_name,email, add,contact,spec,lat,long ))
                print("added")
                mysql.connection.commit()
                query="Select image from sign where name=%s"
                cur.execute(query,(uname,))
                data1=cur.fetchone()
                return render_template('home.html')
            else:
                return("username exits") 

    return render_template('add_rest.html')


@app.route('/res_log', methods=['GET','POST'])
def res_log():
      if request.method == 'POST':
        # Fetch form data
        print("bye")
        userDetails = request.form
        email = userDetails['email']
        password = userDetails['pass']
        cur = mysql.connection.cursor()
        query="Select *from restaurant where email=%s and password=%s"
        cur.execute(query,(email,password,))
        data=cur.fetchall()
        print(data)
        if(data==()):
            return("please create account")
        else:     
             return render_template('home.html')
      return render_template('login.html')
    

app.run(debug=True,port=5500)
