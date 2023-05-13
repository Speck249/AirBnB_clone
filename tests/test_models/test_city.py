#!/usr/bin/python3
"""Unit test suite for City class."""
import unittest
from models.base_model import BaseModel
from models.city import City
import datetime
import time


class TestCity(unittest.TestCase):
    """Handles city test cases."""
    obj = City()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(City("Albany"), BaseModel)
        assert not isinstance(City("Albany"), str)
        assert not isinstance(b, City)

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'state_id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        msg = "instance type error."
        self.assertIsInstance(self.obj.state_id, str, msg)
        self.assertIsInstance(self.obj.name, str, msg)
        self.assertIsInstance(self.obj.id, str, msg)
        self.assertIsInstance(self.obj.created_at,
                      datetime.datetime, msg)
        self.assertIsInstance(self.obj.updated_at,
                      datetime.datetime, msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        city = City("Albany")
        try:
            city.name = "name type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
