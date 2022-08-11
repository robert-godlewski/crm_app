# Main Description
An online app that has a lot of todo list items and can set reminders for the user.  
The data on the table will be organized off of the date they are due (or when the task was created).  
An app inspired by both of Apple's Reminders app and iCal.

Go to http://35.162.237.112/ to see the live website run off of aws-ec2 server.

Currently developing Version 2 build.

# Release Notes
master branch in the repository is the current and up to date material.

version1 branch in the repository is the first initial version I did as one of my personal projects through Coding Dojo:
* Begun the Project and modularize it for future CICD
* Full CRUD of Users
* Full CRUD of Tasks

version2 branch is in current development phase.

# Citing work
For datetime module for class details on the python documentation: https://docs.python.org/3/library/datetime.html
Also look at both Flask and Bootstrap documentation for more info.

# Frameworks used
* Flask (Python)
* Bootstrap (CSS/JavaScript)

# Todos
* Implement html templates for faster reads of code
* Apply some of the Backlog ideas (Read below under Product Backlog Section of this file)
* Instead of outright deleting a task how about adding in another list of tasks done in another table for later reference.
* Use React.js to make the reminder automation smoother, making Flask more like an API - Useful references for Flask-React: https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9

# Website Views - Version 1

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
* Add in a warning page before deleting a user account (Deletion warning page)
* Create a calendar page to see when an where things are due (Calendar View), currently only have List View.
* Add in a notes page and people so that users can interact.
* Create a desktop app version of this app using Docker.
* Create a mobile app version using Swift/Java.

# Development details
Development code is running on http://localhost:8000/

Inorder for the application to work you will need to add in a project_key.py file for sensitive information like mySQL_password (string) and flask_key (string).  Put this file under flask_app/config/.
