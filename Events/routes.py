import psycopg2
from Events import app
from flask import render_template,request,url_for,redirect

bevent=[]
POSTGRESQL_URI="postgres://qaooeuge:3ssa-7dQyeAogu6uQ9OeWtDhVkIv8a9r@topsy.db.elephantsql.com:5432/qaooeuge"
connection=psycopg2.connect(POSTGRESQL_URI)
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE BDAYTB(tbname TEXT, tbvenue TEXT, tbdate TEXT, tbtime TEXT, tbguests INT, tbcate TEXT, tbtheme TEXT, tbemail TEXT, tbphone INT, tbappdate TEXT, tbapptime TEXT);")
except psycopg2.errors.DuplicateTable:
    pass

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')

@app.route('/contact')
def con():
    return render_template('contact.html')

@app.route('/birthday', methods=["GET","POST"])
def birthdayy():
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO BDAYTB VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                            (
                                request.form.get("bname"),
                                request.form.get("bvenue"),
                                request.form.get("bdate"),
                                request.form.get("btime"),
                                request.form.get("bguests"),
                                request.form.get("bcate"),
                                request.form.get("btheme"),
                                request.form.get("bemail"),
                                request.form.get("bphone"),
                                request.form.get("bappdate"),
                                request.form.get("bapptime"),
                            )
                )
        return redirect(url_for('rec'))
    return render_template('birthday.html')

@app.route('/receipt')
def rec():
    with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM BDAYTB order by tbdate desc limit 1;")
                bevent = cursor.fetchall()
    return render_template('receipt.jinja2', evententries=bevent)



@app.route('/Login', methods=["GET","POST"])
def log():
    if request.form.get("semail") != None:
        if request.method == "POST":
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("select pass from customer where email = '%s';" % str(request.form.get("semail")))
                    lst = []
                    lst = cursor.fetchall()
                    tup = lst[0]
                    if tup[0]==request.form.get("spass"):
                        return redirect(url_for('ty'))
                    else:
                        print("password not matched")
    elif request.form.get("remail") != None:
        if request.method == "POST" and request.form.get("rconpass")==request.form.get("rpass"):
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO CUSTOMER VALUES(%s,%s);", (request.form.get("remail"), request.form.get("rconpass")))
            return redirect(url_for('ty'))
    return render_template('login.html')

@app.route('/type')
def ty():
    return render_template('type.html')

@app.route('/ConferenceAndSeminar')
def ConferenceAndSeminar():
    return render_template('ConferenceAndSeminar.html')

@app.route('/wedding')
def wedding():
    return render_template('wedding.html')

@app.route('/Virtual events')
def virtual():
    return render_template('virtual.html')
    
@app.route('/payment')
def pay():
    return render_template('pay.html')