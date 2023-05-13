#!/usr/bin/python3
"""
City Model
"""
from models.base_model import BaseModel

class City(BaseModel):
    """Class inherits from BaseModel.
    Handles city instances.

    Att:
        state_id (str): state Id
        name (str): City name

    """
    state_id, name = "", ""
