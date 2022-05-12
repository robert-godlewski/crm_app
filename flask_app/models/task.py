from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


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
        all_tasks = list()
        for row in results:
            task = cls(row)
            all_tasks.append(task)
        return all_tasks
    
    @classmethod
    def get_task_by_id(cls, data):
        query = "SELECT * FROM tasks WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_task_by_description(cls, data):
        query = "SELECT * FROM tasks where task_description = %(task_description)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_task(cls, data):
        query = '''
        UPDATE tasks
        SET task_description = %(task_description)s, priority = %(priority)s, is_recurring = %(is_recurring)s, reminder_time = %(reminder_time)s, due_date = %(due_date)s, updated_at = NOW()
        WHERE id = %(id)s;
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_task(cls, data):
        query = "DELETE FROM tasks where id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_all_tasks_for_user(cls, data):
        query = "DELETE FROM tasks where user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_task(task):
        is_valid = True
        if len(task['task_description']) < 2:
            flash("Needs to be at least 2 characters long", "create_task")
            is_valid = False
        return is_valid
