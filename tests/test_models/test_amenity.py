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
        """Assert inherited attribute is present."""
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

    def test_inherited_id(self):
        """Assert generated id is unique."""
        obj_a = Amenity()
        a_obj = Amenity()
        self.assertNotEqual(obj_a, a_obj)

    def test_save(self):
        """Assert save() method output.""" 
        obj_a = Amenity()
        time.sleep(0.12)
        initial_update = obj_a.updated_at
        obj_a.save()
        self.assertLess(initial_update, obj_a.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys."""
        obj_a = Amenity()
        self.assertIn("__class__", obj_a.to_dict())
        self.assertIn("id", obj_a.to_dict())
        self.assertIn("created_at", obj_a.to_dict())
        self.assertIn("updated_at", obj_a.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values."""
        obj_a = Amenity()
        obj_a.name = "My First Model"
        obj_a.my_number = 89
        self.assertEqual("My First Model", obj_a.name)
        self.assertIn("my_number", obj_a.to_dict())

    def test_to_dict(self):
        """Assert expected to_dict() method output."""
        msg = "Unexpected output."""
        obj_a = Amenity()
        obj_a.id = "74cb9cb3"
        ts = datetime.today()
        obj_a.created_at = ts
        obj_a.updated_at = ts
        ts_iso = ts.isoformat()
        test_dict = {
            "__class__": "Amenity",
            "id": "74cb9cb3",
            "created_at": ts_iso,
            "updated_at": ts_iso,
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
