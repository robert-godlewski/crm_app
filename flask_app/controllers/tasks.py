from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import user, task
# for datetime functions
from datetime import datetime, date, time


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
    # Converting priority values to integers from strings
    priority = int(request.form['priority'])
    # Assigning is_recurring value 0 (false) / 1 (true)
    if not 'is_recurring' in request.form:
        is_recurring = 0
    elif request.form['is_recurring'] == 'on':
        is_recurring = 1
    # Assigning temporary values to reminder_time and due_date ad default values
    current_datetime = datetime.now()
    current_datetime_str = str(current_datetime)
    current_datetime_list = current_datetime_str.split(' ')
    # Formating reminder_time
    if request.form['reminder_time'] == '':
        current_time_raw = current_datetime_list[1]
        current_time_list = current_time_raw.split(':')
        reminder_time = time(int(current_time_list[0]), int(current_time_list[1]), 0)
    else:
        time_str = request.form['reminder_time']
        time_list = time_str.split(':')
        reminder_time = time(int(time_list[0]), int(time_list[1]), 0)
    # Formating due_date
    if request.form['due_date'] == '':
        current_date_raw = current_datetime_list[0]
        current_date_list = current_date_raw.split('-')
        due_date = date(int(current_date_list[0]), int(current_date_list[1]), int(current_date_list[2]))
    else:
        date_str = request.form['due_date']
        date_list = date_str.split('-')
        due_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    # Assigning all the formated values to database
    data = {
        "task_description": request.form['task_description'],
        "priority": priority,
        "is_recurring": is_recurring,
        "reminder_time": reminder_time,
        "due_date": due_date,
        "user_id": session['user_id']
    }
    print(f"passed in data = {data}")
    task.Task.create_task(data)
    # Temporary redirect to see if it works
    return redirect('/dashboard')

@app.route('/view_task/<int:id>')
def view_task(id): pass

@app.route('/edit_task/<int:id>')
def edit_task(id): pass

@app.route('/update/task', methods=['POST'])
def update_task(): pass

@app.route('/destroy/task/<int:id>')
def destroy_task(id): pass
