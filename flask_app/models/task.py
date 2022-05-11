from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


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

    @classmethod
    def create_task(cls, data):
        query = '''
        INSERT INTO tasks ( task_description, priority, is_recurring, reminder_time, due_date, created_at, updated_at, user_id )
        VALUES ( %(task_description)s, %(priority)s, %(is_recurring)s, %(reminder_time)s, %(due_date)s, NOW(), NOW(), %(user_id)s );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_tasks_for_user(cls, data):
        query = "SELECT * FROM tasks WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        all_tasks = list()
        for row in results:
            task = cls(row)
            print(task)
            all_tasks.append(task)
        print(all_tasks)
        return all_tasks
    
    @classmethod
    def get_task_by_id(cls, data):
        query = "SELECT * FROM tasks WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return cls(results[0])

    @staticmethod
    def validate_task(task):
        is_valid = True
        if len(task['task_description']) < 2:
            flash("Needs to be at least 2 characters long", "create_task")
            is_valid = False
        return is_valid
