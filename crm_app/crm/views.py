# Views handled by the urls.py in the crm app folder
from django.shortcuts import render, HttpResponse

def index(request): return HttpResponse("This is the equivalent of @app.route('/')!")
