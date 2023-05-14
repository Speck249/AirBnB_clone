#!/usr/bin/python3
"""
State Class
"""
from models.base_model import BaseModel

class State(BaseModel):
    """Class inherits from BaseModel.
    Handles state instances.

    Att:
        name (str): state name
    """

    name = ""
