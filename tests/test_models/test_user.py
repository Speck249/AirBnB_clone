#!/usr/bin/python3
"""Unit test suite for User class."""
import unittest
from models.base_model import BaseModel
from models.user import User
import datetime
import time


class TestUser(unittest.TestCase):
    """Handles user test cases."""
    obj = User()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(User("john_doe@gmail.com"), BaseModel)
        assert not isinstance(User("john_doe@gmail.com"), str)
        assert not isinstance(b, User)

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        msg = "instance type error."
        self.assertIsInstance(self.obj.first_name, str, msg)
        self.assertIsInstance(self.obj.last_name, str, msg)
        self.assertIsInstance(self.obj.email, str, msg)
        self.assertIsInstance(self.obj.password, str, msg)
        self.assertIsInstance(self.obj.id, str, msg)
        self.assertIsInstance(self.obj.created_at,
                      datetime.datetime, msg)
        self.assertIsInstance(self.obj.updated_at,
                      datetime.datetime, msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        user = User("s!mp3pa$$w0rd")
        try:
            user.password = "password type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
