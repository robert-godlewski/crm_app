# Views handled by the urls.py in the crm app folder
from django.shortcuts import render, redirect, HttpResponse

def index(request): 
    # Test to see that the route is working
    #return HttpResponse("This is the equivalent of @app.route('/')!")
    return render(request, "index.html")

def create_user(request):
    print("Got Post Info.............")
    print(request.POST)
    fName = request.POST["fName"]
    lName = request.POST["lName"]
    # Need to validate the email so that it has the @ sign
    email = request.POST["email"]
    # Password needs to havy Bcrypt and to match with conf_password
    password = request.POST["password"]
    # Don't save conf_password to the database or pass through
    conf_password = request.POST["conf_password"]
    # New variables to add to the database or just put it in the model
    todo_list = []
    todos_done = 0
    # What to pass through to the database
    user_info = {
        "fName": fName,
        "lName": lName,
        "email": email,
        "password": password,
        "todo_list": todo_list,
        "todos_done": todos_done
    }
    # Need to save the user_info to a database
    return render(request, template_name="dashboard.html", context=user_info)

def login(request): 
    # Need to be able to acess the database to grab the login info needed to render the page
    # Replace what context is equal to with the data grabed from the database
    #return render(request, template_name="dashboard.html", context=...)
    return HttpResponse("This will need to route to the Dashboard but need the necessary data!")
