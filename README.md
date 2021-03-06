# Main Description
An online app that has a lot of todo list items and can set reminders for the user.  
The data on the table will be organized off of the date they are due (or when the task was created).  
A combo of both iCal and reminders on the iPhone/Mac.

Development code is running on http://localhost:8000/

Inorder for the application to work you will need to add in a project_key.py file for sensitive information like mySQL_password (string) and flask_key (string).  Put this file under flask_app/config/.

# Frameworks used
* Flask (Python)
* Bootstrap (CSS/JavaScript)

# Website_views

## Login and registration (home page)
![Login and Registration](/crm_images/login_signup.png)

## Dashboard
![The Users Dashboard to view all tasks](/crm_images/users_dashboard.png)

## Viewing (and deleting) User's details
![View everything about the user](/crm_images/user_details.png)

## Editing user info
![Editing the user](/crm_images/editing_user_info.png)

## Adding in new tasks
![Creating new tasks todo](/crm_images/adding_new_task.png)

## Viewing task details
![Reading details of the task selected](/crm_images/task_details.png)

## Editing a task
![Editing task information](/crm_images/editing_a_task.png)

# Product Backlog
* Create an automation email reminder to send to the user about their assigned task.
* Add in a warning page before deleting an account
* Create a calendar page to see when an where things are due.
* Add in a notes page and people so that users can interact.
* Create a desktop app version of this app.
* Create a mobile app version using Swift/Java (need to learn both of these languages)

# Citing work
For datetime module for class details on the python documentation: https://docs.python.org/3/library/datetime.html
Also look at both Flask and Bootstrap documentation for more info.
