#!/usr/bin/python3
"""
Place Class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class inherits from BaseModel.
    Handles Place Instances.

    Att:
        city_id (str): city Id
        user_id (str): user Id
        name (str): place name
        description (str): place descriptipn
        number_rooms (int): no. rooms
        number_bathrooms (int): no. bathrooms
        max_guest (int): no. guests
        price_by_night (int): price
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
