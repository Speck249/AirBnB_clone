#!/usr/bin/python3
"""Unit test suite for Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import datetime
import time


class TestAmenity(unittest.TestCase):
    """Handles amenity test cases."""
    obj = Amenity()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        a =  BaseModel()
        assert isinstance(Amenity("Hospitals"), BaseModel)
        assert not isinstance(Amenity("Hospitals"), str)
        assert not isinstance(a, Amenity)

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        msg = "instance type error."
        self.assertIsInstance(self.obj.id, str, msg)
        self.assertIsInstance(self.obj.name, str, msg)
        self.assertIsInstance(self.obj.created_at, datetime.datetime, msg)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime, msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        b = Amenity("Schools")
        try:
            b.name = "name type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
