#!/usr/bin/python3
"""Unit test suite for Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review
import datetime
import time


class TestReview(unittest.TestCase):
    """Handles review test cases."""
    obj = Review()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(Review("Everything was perfect"), BaseModel)
        assert not isinstance(Review("Everything was perfect"), str)
        assert not isinstance(b, Review)

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'place_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'text'))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        msg = "instance type error."
        self.assertIsInstance(self.obj.place_id, str, msg)
        self.assertIsInstance(self.obj.user_id, str, msg)
        self.assertIsInstance(self.obj.text, str, msg)
        self.assertIsInstance(self.obj.id, str, msg)
        self.assertIsInstance(self.obj.created_at, 
                      datetime.datetime, msg)
        self.assertIsInstance(self.obj.updated_at, 
                      datetime.datetime, msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        review = Review("Everything was perfect, "
                "would love to come again")
        try:
            review.text = "text type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
