#!/usr/bin/python3
"""
City Model
"""
from models.base_model import BaseModel

class City(BaseModel):
    """City Instance

    Att:
        state_id (str): state Id
        name (str): City name

    """
    state_id, name = "", ""
