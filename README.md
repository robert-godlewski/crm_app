# Main Description
An online app that has a lot of todo list items and can set reminders for the user.  
The data on the table will be organized off of the date they are due (or when the task was created).  
A combo of both iCal and reminders on the iPhone/Mac.

# Frameworks used
* Django (Python)
* Bootstrap (CSS)

# Product Backlog
* Create an automation email reminder to send to the user about their assigned task.
* Create a calendar page to see when an where things are due.
* Add in a notes page and people so that users can interact.
* Create a desktop app version of this app.
* Create a mobile app version using Swift/Java (need to learn both of these languages)

# Django env
Running on http://localhost:8000/

Activating env: 
{root folder} % source crmDjangoEnv/bin/activate

Running the server: 
(crmDjangoEnv) ... crm_app % python3 manage.py runserver

Initialising Migrations in the app:
(crmDjangoEnv) ... crm_app % python3 manage.py makemigrates

Running migrations to update the models of the app: 
(crmDjangoEnv) ... crm_app % python3 manage.py migrate

Deactivating env: 
(crmDjangoEnv) ... {root folder} % deactivate

# Other Django code only use once:
Creating an venv: % python3 -m venv crmDjangoEnv

Starting a Django project: (crmDjangoEnv) ... % django-admin startproject crm_app
