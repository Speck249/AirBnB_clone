#!/usr/bin/python3
"""
Amenity Class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class inherits from BaseModel.
    Handles Amenity Instance.
    
    Att:
        name (str): amenity name
    """
    
    name = ""
