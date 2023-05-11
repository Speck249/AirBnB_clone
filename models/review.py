#!/usr/bin/python3
"""Module presents class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class inherits from BaseModel.
    Handles review instances.

    Att:
        place_id (str): Place Id
        user_id (str) User Id
        text (str): review text
    """

        place_id, user_id = "", ""
        text = ""
