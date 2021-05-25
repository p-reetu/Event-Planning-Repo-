import psycopg2
from Events import app
from flask import render_template,request,url_for,redirect

bevent=[]
wevent=[]
csevent=[]
POSTGRESQL_URI="postgres://qaooeuge:3ssa-7dQyeAogu6uQ9OeWtDhVkIv8a9r@topsy.db.elephantsql.com:5432/qaooeuge"
connection=psycopg2.connect(POSTGRESQL_URI)
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE BDAYTB(tbid TEXT PRIMARY KEY, tbname TEXT, tbvenue TEXT, tbdate TEXT, tbtime TEXT, tbguests INT, tbcate TEXT, tbtheme TEXT, tbemail TEXT, tbphone INT, tbappdate TEXT, tbapptime TEXT);")
except psycopg2.errors.DuplicateTable:
    pass

@app.route('/')
@app.route('/home')
def homepage():
    '''with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT tbguests FROM BDAYTB order by tbdate desc limit 1;")
                test = []
                test = cursor.fetchall()
                num = test[0]
                print(num[0]+1)
                print('B'+str(num[0]+1))'''
    return render_template('homepage.html')

@app.route('/About Us')
def au():
    return render_template('AboutUs.html')

@app.route('/contact')
def con():
    return render_template('contactus.html')

@app.route('/birthday', methods=["GET","POST"])
def birthdayy():
    try:
        with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT tbid FROM BDAYTB order by tbid desc limit 1;")
                    test = []
                    test = cursor.fetchall()
                    num = test[0]
                    s1 = num[0]
                    s2 = 'B'
                    if s1.startswith(s2):
                        s3 = s1.replace(s2, '')
                    imp = int(s3)+1
    except:
        imp=1
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO BDAYTB VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                            (
                                'B'+str(imp),
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
                cursor.execute("SELECT * FROM BDAYTB order by tbid desc limit 1;")
                bevent = cursor.fetchall()
    return render_template('receipt.jinja2', evententries=bevent)

@app.route('/receiptw')
def recw():
    with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM WEDTB order by twid desc limit 1;")
                wevent = cursor.fetchall()
    return render_template('receiptw.jinja2', evententries=wevent)

@app.route('/receiptcs')
def reccs():
    with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM CSTB order by tcid desc limit 1;")
                csevent = cursor.fetchall()
    return render_template('receiptcs.jinja2', evententries=csevent)

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

@app.route('/ConferenceAndSeminar', methods=["GET", "POST"])
def ConferenceAndSeminar():
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT tcid FROM CSTB order by tcid desc limit 1;")
                test = []
                test = cursor.fetchall()
                num = test[0]
                s1 = num[0]
                s2 = 'C'
                if s1.startswith(s2):
                    s3 = s1.replace(s2, '')
                imp = int(s3)+1
    except:
        imp=1
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO CSTB VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                            (
                                'C'+str(imp),
                                request.form.get("ctitle"),
                                request.form.get("ctype"),
                                request.form.get("cdate"),
                                request.form.get("ctime"),
                                request.form.get("cspsname"),
                                request.form.get("cspkname"),
                                request.form.get("cbudget"),
                                request.form.get("cguests"),
                                request.form.get("ccate"),
                                request.form.get("cservices"),
                                request.form.get("cemail"),
                                request.form.get("cphone"),
                                request.form.get("cappdate"),
                                request.form.get("capptime"),
                            )
                )
        return redirect(url_for('reccs'))
    return render_template('ConferenceAndSeminar.html')

@app.route('/wedding', methods=["GET", "POST"])
def wedding():
    try:
        with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT twid FROM WEDTB order by twid desc limit 1;")
                    test = []
                    test = cursor.fetchall()
                    num = test[0]
                    s1 = num[0]
                    s2 = 'W'
                    if s1.startswith(s2):
                        s3 = s1.replace(s2, '')
                    imp = int(s3)+1
    except:
        imp=1
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO WEDTB VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                            (
                                'W'+str(imp),
                                request.form.get("wname"),
                                request.form.get("wvenue"),
                                request.form.get("wdate"),
                                request.form.get("wtime"),
                                request.form.get("wguests"),
                                request.form.getlist("check1"),
                                request.form.get("writuals"),
                                request.form.getlist("check2"),
                                request.form.get("wtheme"),
                                request.form.get("wemail"),
                                request.form.get("wphone"),
                                request.form.get("wappdate"),
                                request.form.get("wapptime"),
                            )
                )
        return redirect(url_for('recw'))
    return render_template('wedding.html')

@app.route('/Virtual events', methods=["GET","POST"])
def virtual():
    if request.method == "POST":
        return redirect(url_for('vir'))
    return render_template('virtual.html')

@app.route('/book it')
def vir():
    return render_template('virtualeve.html') 
    
@app.route('/payment')
def pay():
    return render_template('pay.html')
