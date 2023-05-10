#!/usr/bin/python3
"""
Review Model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Review Instance

    Att:
        place_id (str): Place Id
        user_id (str) User Id
        text (str): review text
    """

        place_id, user_id = "", ""
        text = ""
