from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        "fName": request.form['fName'],
        "lName": request.form['lName'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user_in_db = User.get_user_by_email(request.form)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template("dashboard.html", user=user)

@app.route('/view_user/<int:id>')
def view_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    return render_template("view_user.html", user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
