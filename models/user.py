#!/usr/bin/python3
"""
User class
"""
<<<<<<< HEAD
from models import BaseModel
=======
from models.base_model import BaseModel

>>>>>>> d6106ffb420be867ae15e410a0841f35099b0380

class User(BaseModel):
    """Instance of a User

    Att:
        email (str): email address
        password (str): user password
        first_name (str): 1st name
        last_name (str): last name
<<<<<<< HEAD

    """
=======
    """

>>>>>>> d6106ffb420be867ae15e410a0841f35099b0380
    email, password = "", ""
    first_name, last_name = "", ""
