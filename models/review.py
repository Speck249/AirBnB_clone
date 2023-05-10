#!/usr/bin/python3
"""
Review Model
"""
<<<<<<< HEAD
from models import BaseModel

class City(BaseModel):
=======
from models.base_model import BaseModel


class Review(BaseModel):
>>>>>>> d6106ffb420be867ae15e410a0841f35099b0380
    """Review Instance

    Att:
        place_id (str): Place Id
        user_id (str) User Id
        text (str): review text
<<<<<<< HEAD

        """
=======
    """
>>>>>>> d6106ffb420be867ae15e410a0841f35099b0380

        place_id, user_id = "", ""
        text = ""
