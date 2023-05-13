#!/usr/bin/python3
"""Unit test suite for Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place
import datetime
import time


class TestPlace(unittest.TestCase):
    """Handles place test cases."""
    obj = Place()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(Place(73.756233), BaseModel)
        assert not isinstance(Place(73.756233), float)
        assert not isinstance(b, Place)

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'city_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'description'))
        self.assertTrue(hasattr(self.obj, 'number_rooms'))
        self.assertTrue(hasattr(self.obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.obj, 'max_guest'))
        self.assertTrue(hasattr(self.obj, 'price_by_night'))
        self.assertTrue(hasattr(self.obj, 'latitude'))
        self.assertTrue(hasattr(self.obj, 'longitude'))
        self.assertTrue(hasattr(self.obj, 'amenity_ids'))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        msg = "instance type error."
        self.assertIsInstance(self.obj.city_id, str, msg)
        self.assertIsInstance(self.obj.user_id, str, msg)
        self.assertIsInstance(self.obj.name, str, msg)
        self.assertIsInstance(self.obj.description, str, msg)
        self.assertIsInstance(self.obj.number_rooms, int, msg)
        self.assertIsInstance(self.obj.number_bathrooms, int, msg)
        self.assertIsInstance(self.obj.max_guest, int, msg)
        self.assertIsInstance(self.obj.price_by_night, int, msg)
        self.assertIsInstance(self.obj.latitude, float, msg)
        self.assertIsInstance(self.obj.longitude, float, msg)
        self.assertIsInstance(self.obj.amenity_ids, list, msg)
        self.assertIsInstance(self.obj.id, str, msg)
        self.assertIsInstance(self.obj.created_at,
                      datetime.datetime, msg)
        self.assertIsInstance(self.obj.updated_at,
                      datetime.datetime, msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        place = Place(73.756233)
        try:
            place.longitude = "longitude type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
