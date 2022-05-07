from django.db import models

# Create your models here.
class User(models.Model):
    #def __init__(self):
    # id field is implicit
    #id = models.IntegerField()
    fName = models.CharField(max_length=45)
    lName = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    todos_done = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='../crm/static/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    task_description = models.TextField()
    priority = models.PositiveIntegerField()
    is_recurring = models.BooleanField(default=False)
    due_date = models.DateTimeField(auto_now=False)
    reminder_time = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
