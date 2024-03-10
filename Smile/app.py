from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/20157/OneDrive - Wellington College/13 DT/cafeProject/Smile/smile.db"

app = Flask(__name__)

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu/<cat_id>')
def render_menu_page(cat_id):
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products WHERE cat_id=?"
    cur = con.cursor()
    cur.execute(query, (cat_id, ))
    product_list = cur.fetchall()
    query = "SELECT id,name FROM category"
    cur = con.cursor()
    cur.execute(query)
    category_list = cur.fetchall()
    con.close()
    print(product_list)
    return render_template('menu.html', products=product_list, categories=category_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')

@app.route('/login', methods=['POST', 'GET'])
def render_login_page():
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def render_signup_page():
    if request.method('POST'):
        print(request.form)
        fname = request.form.get('fname').title().strip()
        lname = request.form.get('lname').title().strip()
        email = request.form.get('email').lower().strip()
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if password != password2:
            return redirect("/signup?error=Passwords+do+not+match")

        if password < 8:
            return redirect("/signup?error=Password+must+be+at+least+8+letters")

        con = open_database('DATABASE')
        query = 'INSERT INTO user (fname, lname, email, password) VALUES (?, ?, ?, ?)'

        try:
            cur.execute(query, (fname, lname, email, password))

    return render_template('signup.html')


app.run(host='0.0.0.0', debug=True)
