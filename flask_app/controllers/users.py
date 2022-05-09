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
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
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

@app.route('/edit_user/<int:id>')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    print(f"user info at the start of the edit_user route: {user}")
    return render_template("edit_user.html", user=user)

@app.route('/update/user', methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    if not User.validate_user(request.form, False):
        return redirect(f"/edit_user/{request.form['id']}")
    print(f"Form Data: {request.form}")
    data = {
        "id": request.form['id'],
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    User.update_user(data)
    user_id = request.form['id']
    return redirect(f"/view_user/{user_id}")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
