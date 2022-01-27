from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails ( email, created_at, updated_at ) VALUES (%(email)s, Now(), Now());"
        return MySQLConnection("email_validation").query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = MySQLConnection("email_validation").query_db(query)
        emails = []
        for e in results:
            emails.append(cls(e))
        return emails
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        data=Email.get_all()
        if not EMAIL_REGEX.match(email["email"]):
            flash("Email is invalid")
            is_valid = False
        for d in data:
            if d.email == email["email"]:
                flash("email already used")
                is_valid = False
        return is_valid