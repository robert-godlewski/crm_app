# Main Description
An online app that has a lot of todo list items and can set reminders for the user.  
The data on the table will be organized off of the date they are due (or when the task was created).  
A combo of both iCal and reminders on the iPhone/Mac.

# Frameworks used
* Flask (Python)
* Bootstrap (CSS)

# Product Backlog
* Create an automation email reminder to send to the user about their assigned task.
* Create a calendar page to see when an where things are due.
* Add in a notes page and people so that users can interact.
* Create a desktop app version of this app.
* Create a mobile app version using Swift/Java (need to learn both of these languages)

# Flask env
Running on http://localhost:8000/

Activating virtual environment:
{root folder} % pipenv shell

Deactivating virtual environment:
(root folder name) ... % exit

# Other Flask code only use once
Creating env using pip:
{root folder} % pip3 install pipenv

Installing flask:
(root folder) ... % pipenv install flask flask-bcrypt PyMySQL flash
