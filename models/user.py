#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class inherits from BaseModel.
    Handles user instances.

    Att:
        email (str): email address
        password (str): user password
        first_name (str): 1st name
        last_name (str): last name
    """

    email, password = "", ""
    first_name, last_name = "", ""
