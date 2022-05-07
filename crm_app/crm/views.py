# Views handled by the urls.py in the crm app folder
from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request): 
    # Test to see that the route is working
    #return HttpResponse("This is the equivalent of @app.route('/')!")
    return render(request, "index.html")

def create_user(request):
    print("Got Post Info.............")
    print(request.POST)
    fName = request.POST["fName"]
    #print(f"First Name is {fName}")
    lName = request.POST["lName"]
    #print(f"Last Name is {lName}")
    # Need to validate the email so that it has the @ sign
    email = request.POST["email"]
    #print(f"Email is {email}")
    # Password needs to havy Bcrypt and to match with conf_password
    password = request.POST["password"]
    #print(f"Password is {password}")
    # Don't save conf_password to the database or pass through
    conf_password = request.POST["conf_password"]
    #print(f"Confirmation Password is {conf_password}")
    # Use this temporarily until we add in Bcrypt
    if password != conf_password: 
        print("Cannot create user")
        return render(request, template_name="index.html")
    User.objects.create(fName=fName, lName=lName, email=email, password=password, todos_done=0)
    ########## for testing the database
    #all_users = User.objects.all()
    #print(f"All users: {all_users}")
    # Need to grab the same user created from before
    new_user = User.objects.filter(email=email)[0]
    print(f"New user: {new_user}")
    print(f"First Name: {new_user.fName}")
    print(f"Last Name: {new_user.lName}")
    print(f"Email: {new_user.email}")
    print(f"Password: {new_user.password}")
    print(f"Todos Done: {new_user.todos_done}")
    request.session = {
        "fName": new_user.fName,
        "lName": new_user.lName,
        "email": new_user.email,
        "password": new_user.password,
        "todos_done": new_user.todos_done
    }
    print(f"session data: {request.session}")
    #return render(request, template_name="dashboard.html", context=context)
    return redirect("/login")

# Need to figure out a way to grab data and add it to the login
def login(request):
    context = {
        "fName": request.session["fName"],
        "lName": request.session["lName"],
        "email": request.session["email"],
        "password": request.session["password"],
        "todos_done": request.session["todos_done"]
    }
    print(f"context data: {context}")
    return render(request, template_name="dashboard.html", context=context)

def logout(request):
    # will need to clear the session
    request.session.clear()
    return render(request, template_name="index.html")
