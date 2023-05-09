#!/usr/bin/python3
"""
User class
"""
from models import BaseModel

class User(BaseModel):
    """Instance of a User

    Att:
        email (str): email address
        password (str): user password
        first_name (str): 1st name
        last_name (str): last name

    """
    email, password = "", ""
    first_name, last_name = "", ""
