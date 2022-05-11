from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import user, task
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    if not user.User.validate_user(request.form):
        return redirect('/')
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = user.User.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user_in_db = user.User.get_user_by_email(request.form)
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
    user_id = session['user_id']
    user_info = user.User.get_user_by_id({"id": user_id})
    tasks = task.Task.get_all_tasks_for_user({"user_id": user_id})
    return render_template("dashboard.html", user=user_info, tasks=tasks, task_num=len(tasks))

@app.route('/view_user/<int:id>')
def view_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    user_info = user.User.get_user_by_id({"id": id})
    tasks = task.Task.get_all_tasks_for_user({"user_id": id})
    tasks_length = len(tasks)
    return render_template("view_user.html", user=user_info, tasks_num=tasks_length)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    user_info = user.User.get_user_by_id({"id": id})
    return render_template("edit_user.html", user=user_info)

@app.route('/update/user', methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    if not user.User.validate_user(request.form, False):
        return redirect(f"/edit_user/{request.form['id']}")
    data = {
        "id": request.form['id'],
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    user.User.update_user(data)
    user_id = request.form['id']
    return redirect(f"/view_user/{user_id}")

@app.route('/destroy/user/<int:id>')
def destroy_user_and_tasks(id):
    if 'user_id' not in session:
        return redirect('/logout')
    task.Task.delete_all_tasks_for_user({"user_id": id})
    print("Deleted all tasks....")
    # Then delete the user - This currently works as it should
    user.User.delete_user({"id": id})
    print("Deleted User.")
    return redirect('/logout')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
