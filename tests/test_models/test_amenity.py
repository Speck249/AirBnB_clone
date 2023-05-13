#!/usr/bin/python3
"""Unit test suite for Amenity class."""
import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import time


class TestAmenity(unittest.TestCase):
    """Handles amenity test cases."""
    obj = Amenity()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(Amenity, BaseModel))

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

    def test_basemodel_uuid(self):
        """Assert generated id is unique."""
        obj_a = Amenity()
        obj_b = Amenity()
        self.assertNotEqual(obj_a, obj_b)

    def test_save(self):
        obj_a = Amenity()
        time.sleep(0.12)
        initial_update = obj_a.update_at
        obj_a.save()
        self.assertLess(initial_update, obj_a.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys inside dict"""
        obj_a = Amenity()
        self.assertIn("__class__", obj_a.to_dict())
        self.assertIn("id", obj_a.to_dict())
        self.assertIn("created_at", obj_a.to_dict())
        self.assertIn("updated_at", obj_a.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values within dict."""
        obj_a = Amenity()
        obj_a.name = "My First Model"
        obj_a.my_number = 89
        self.assertEqual("My First Model", obj_a.name)
        self.assertIn("my_number", obj_a.to_dict())

    def test_to_dict(self):
        """Assert expected method output."""
        msg = "Unexpected output."""
        obj_a = Amenity()
        ts = datetime.today()
        ts_iso = ts.isoformat()
        obj_a.id = "74cb9cb3-bb94-438b-af2b-7889aef86a8d"
        obj_a.created_at = ts
        obj_a.updated_at = ts
        test_dict = {
            "__class__": "Amenity",
            "id": "74cb9cb3-bb94-438b-" \
            "af2b-7889aef86a8d",
            "created_at": ts,
            "updated_at": ts,
        }
        self.assertDictEqual(test_dict, obj_a.to_dict(), msg)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        amenity = Amenity("Hospitals")
        try:
            amenity.name = "name type error"
        except Exception as e:
            assert isinstance(e, TypeError)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(Amenity("Hospitals"), BaseModel)
        assert not isinstance(Amenity("Hospitals"), str)
        assert not isinstance(b, Amenity)

if __name__ == '__main__':
    unittest.main()
