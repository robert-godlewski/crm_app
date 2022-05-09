#from flask import flash
#from flask_app.config.mysqlconnection import connectToMySQL
#from flask_app.models.user import User


class Task:
    db_name = "crm_schema"

    def __init__(self, data):
        self.id = data['id']
        self.task_description = data['task_description']
        self.priority = data['priority']
        self.is_recurring = data['is_recurring']
        self.due_date = data['due_date']
        self.reminder_time = data['reminder_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
