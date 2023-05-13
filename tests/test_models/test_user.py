#!/usr/bin/python3
"""Unit test suite for User class."""
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import time


class TestUser(unittest.TestCase):
    """Handles user test cases."""
    obj = User()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_id_attribute_exists(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))

    def test_id_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.first_name, str)
        self.assertIsInstance(self.obj.last_name, str)
        self.assertIsInstance(self.obj.email, str)
        self.assertIsInstance(self.obj.password, str)
        self.assertIsInstance(self.obj.id, str)
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_inherited_id(self):
        """Assert generated id is unique."""
        obj_u = User()
        u_obj = User()
        self.assertNotEqual(obj_u, u_obj)

    def test_save(self):
        obj_u = User()
        time.sleep(0.12)
        initial_update = obj_u.updated_at
        obj_u.save()
        self.assertLess(initial_update, obj_u.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys inside dict"""
        obj_u = User()
        self.assertIn("__class__", obj_u.to_dict())
        self.assertIn("id", obj_u.to_dict())
        self.assertIn("created_at", obj_u.to_dict())
        self.assertIn("updated_at", obj_u.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values within dict."""
        obj_u = User()
        obj_u.name = "My First Model"
        obj_u.my_number = 89
        self.assertEqual("My First Model", obj_u.name)
        self.assertIn("my_number", obj_u.to_dict())

    def test_to_dict(self):
        """Assert expected method output."""
        msg = "Unexpected output."""
        obj_u = User()
        obj_u.id = "74cb9cb3"
        ts = datetime.today()
        obj_u.created_at = ts
        obj_u.updated_at = ts
        ts_iso = ts.isoformat()
        test_dict = {
            "__class__": "User",
            "id": "74cb9cb3",
            "created_at": ts_iso,
            "updated_at": ts_iso,
        }

        self.assertDictEqual(obj_u.to_dict(), test_dict, msg)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(User("john_doe@gmail.com"), BaseModel)
        assert not isinstance(User("john_doe@gmail.com"), str)
        assert not isinstance(b, User)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        user = User("s!mp3pa$$w0rd")
        try:
            user.password = "password type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
