from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import user, task
# for datetime functions
from datetime import datetime, date, time


# Funtions to cleanup the inputed code for the database
# form = request.form
def data_clean(form):
    clean_data = dict()
    # Converting priority values to integers from strings
    clean_data['priority'] = int(form['priority'])
    if not 'is_recurring' in form:
        is_recurring = 0
    elif form['is_recurring'] == 'on':
        is_recurring = 1
    clean_data['is_recurring'] = is_recurring
    # Creating temporary time variables that might go into the database
    current_datetime = datetime.now()
    current_datetime_str = str(current_datetime)
    current_datetime_list = current_datetime_str.split(' ')
    # Formating reminder_time
    if form['reminder_time'] == '':
        current_time_raw = current_datetime_list[1]
        current_time_list = current_time_raw.split(':')
        reminder_time = time(int(current_time_list[0]), int(current_time_list[1]), 0)
    else:
        time_str = form['reminder_time']
        time_list = time_str.split(':')
        reminder_time = time(int(time_list[0]), int(time_list[1]), 0)
    clean_data['reminder_time'] = reminder_time
    # Formating due_date
    if form['due_date'] == '':
        current_date_raw = current_datetime_list[0]
        current_date_list = current_date_raw.split('-')
        due_date = date(int(current_date_list[0]), int(current_date_list[1]), int(current_date_list[2]))
    else:
        date_str = form['due_date']
        date_list = date_str.split('-')
        due_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    clean_data['due_date'] = due_date
    return clean_data


# Routes
@app.route('/new_task')
def new_task():
    if 'user_id' not in session:
        return redirect('/logout')
    user_info = user.User.get_user_by_id({"id": session['user_id']})
    return render_template("new_task.html", user=user_info)

@app.route('/create_task', methods=['POST'])
def create_task():
    if 'user_id' not in session:
        return redirect('/logout')
    # Validating the contents in the task description
    if not task.Task.validate_task(request.form):
        return redirect('/new_task')
    # Cleaning up the inputed data
    clean_form_data = data_clean(request.form)
    data = {
        "task_description": request.form['task_description'],
        "priority": clean_form_data['priority'],
        "is_recurring": clean_form_data['is_recurring'],
        "reminder_time": clean_form_data['reminder_time'],
        "due_date": clean_form_data['due_date'],
        "user_id": session['user_id']
    }
    task.Task.create_task(data)
    new_task_created = task.Task.get_task_by_description(data)
    return redirect(f"/view_task/{new_task_created.id}")

@app.route('/view_task/<int:id>')
def view_task(id): 
    if 'user_id' not in session:
        return redirect('/logout')
    task_info = task.Task.get_task_by_id({"id": id})
    return render_template("view_task.html", task=task_info)

@app.route('/edit_task/<int:id>')
def edit_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    task_info = task.Task.get_task_by_id({"id": id})
    return render_template("edit_task.html", task=task_info)

@app.route('/update/task', methods=['POST'])
def update_task():
    if 'user_id' not in session:
        return redirect('/logout')
    if not task.Task.validate_task(request.form):
        return redirect(f"/edit_task/{request.form['id']}")
    # Cleaning up the inputed data
    task_id = int(request.form['id'])
    clean_form_data = data_clean(request.form)
    task_data = {
        "id": task_id,
        "task_description": request.form['task_description'],
        "priority": clean_form_data['priority'],
        "is_recurring": clean_form_data['is_recurring'],
        "reminder_time": clean_form_data['reminder_time'],
        "due_date": clean_form_data['due_date'],
        "user_id": session['user_id']
    }
    task.Task.update_task(task_data)
    return redirect(f"/view_task/{task_id}")

@app.route('/destroy/task/<int:id>')
def destroy_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    print(f"Deleting task and updating todos finished")
    task.Task.delete_task({"id": id})
    # Updating the todos_fin count for users
    user_info = user.User.get_user_by_id({"id": session['user_id']})
    user_info.todos_fin += 1
    user_data = {
        "id": user_info.id,
        "todos_fin": user_info.todos_fin
    }
    user.User.update_user_todo_fin_count(user_data)
    return redirect('/dashboard')
