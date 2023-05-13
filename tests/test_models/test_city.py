#!/usr/bin/python3
"""Unit test suite for City class."""
import unittest
import models
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
import time


class TestCity(unittest.TestCase):
    """Handles city test cases."""
    obj = City()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_name_attribute_exists(self):
        """Assert subclass attribute is present."""
         self.assertTrue(hasattr(self.obj, 'state_id'))

    def test_name_attribute_exists(self):
        """Assert subclass attribute is present."""
        self.assertTrue(hasattr(self.obj, 'name'))

    def test_id_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'id'))

    def test_created_at_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'created_at'))

    def test_updated_at_attribute_exists(self):
        """Assert inherited attribute exist."""
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.state_id, str)

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.name, str)

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.id, str)

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertEqual(datetime, type(self.obj.created_at))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_inherited_id(self):
        """Assert generated id is unique."""
        obj_c = City()
        c_obj = City()
        self.assertNotEqual(obj_c, c_obj)

    def test_save(self):
        obj_c = City()
        time.sleep(0.12)
        initial_update = obj_c.update_at
        obj_c.save()
        self.assertLess(initial_update, obj_c.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys inside dict"""
        obj_c = City()
        self.assertIn("__class__", obj_c.to_dict())
        self.assertIn("id", obj_c.to_dict())
        self.assertIn("created_at", obj_c.to_dict())
        self.assertIn("updated_at", obj_c.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values within dict."""
        obj_c = City()
        obj_c.name = "My First Model"
        obj_c.my_number = 89
        self.assertEqual("My First Model", obj_c.name)
        self.assertIn("my_number", obj_c.to_dict())

    def test_to_dict(self):
        """Assert expected method output."""
        msg = "Unexpected output."""
        obj_c = City()
        ts = datetime.today()
        ts_iso = ts.isoformat()
        obj_c.id = "74cb9cb3-bb94-438b-af2b-7889aef86a8d"
        obj_c.created_at = ts
        obj_c.updated_at = ts
        test_dict = {
            "__class__": "City",
            "id": "74cb9cb3-bb94-438b-" \
            "af2b-7889aef86a8d",
            "created_at": ts,
            "updated_at": ts,
        }
        self.assertDictEqual(test_dict, obj_c.to_dict(), msg)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(City("Albany"), BaseModel)
        assert not isinstance(City("Albany"), str)
        assert not isinstance(b, City)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        city = City("Albany")
        try:
            city.name = "name type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
