from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# email address validations
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')


class User:
    db_name = "crm_schema"

    def __init__(self, data):
        self.id = data['id']
        self.fName = data['fName']
        self.lName = data['lName']
        self.email = data['email']
        self.password = data['password']
        self.todos_done = data['todos_done']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self): 
        return self.fName + " " + self.lName

    @classmethod
    def create_user(cls, data):
        query = '''
        INSERT INTO users ( fName, lName, email, password, todos_done, created_at, updated_at )
        VALUES ( %(fName)s, %(lName)s, %(email)s, %(password)s, 0, NOW(), NOW() );
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1: return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query, user)
        print(user)
        if len(user['fName']) < 2:
            flash("First Name must be at least 2 characters.", "create_user")
            is_valid = False
        if len(user['lName']) < 2:
            flash("Last Name must be at least 2 characters.", "create_user")
            is_valid = False
        if len(results) >= 1:
            flash("Email is already taken.", "create_user")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "create_user")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "create_user")
            is_valid = False
        if user['password'] != user['conf_password']:
            flash("Passwords do not match.", "create_user")
            is_valid = False
        return is_valid
