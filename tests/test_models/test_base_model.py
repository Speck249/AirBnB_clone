#!/usr/bin/python3
"""Unit test suite for BaseModel class."""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Handles base_model test cases."""
    obj = BaseModel()

    def test_basemodel_instantiation(self):
        """Assert parent class constructor."""
        unique_id = "74cb9cb3"
        ts = datetime.today()
        iso_ts = ts.isoformat()
        obj_b = BaseModel(id=unique_id, created_at=iso_ts,
                  updated_at=iso_ts)
        self.assertEqual(obj_b.id, unique_id)
        self.assertEqual(obj_b.created_at, ts)
        self.assertEqual(obj_b.updated_at, ts)

    def test_uuid_exists(self):
        """Assert base_model has public instance id."""
        self.assertTrue(hasattr(self.obj, 'id'))

    def test_created_at_exists(self):
        """Assert base_model has public instance created_at."""
        self.assertTrue(hasattr(self.obj, 'created_at'))

    def test_updated_id_exists(self):
        """Assert base model has public instance updated_at."""
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_basemodel_uuid_type(self):
        """Assert attribute type."""
        self.assertIsInstance(self.obj.id, str)

    def test_basemodel_datetime_type(self):
        """Assert attribute type."""
        self.assertEqual(datetime, type(self.obj.created_at))

    def test_basemodel_datetime_type(self):
        """Assert attribute type."""
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_basemodel_uuid(self):
        """Assert unique id generation."""
        b_obj = BaseModel()
        obj_b = BaseModel()
        self.assertNotEqual(b_obj, obj_b)

    def test_save(self):
        """Assert save() method output."""
        obj_b = BaseModel()
        time.sleep(0.12)
        initial_update = obj_b.updated_at
        obj_b.save()
        self.assertLess(initial_update, obj_b.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys."""
        obj_b = BaseModel()
        self.assertIn("__class__", obj_b.to_dict())
        self.assertIn("id", obj_b.to_dict())
        self.assertIn("created_at", obj_b.to_dict())
        self.assertIn("updated_at", obj_b.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values."""
        obj_b = BaseModel()
        obj_b.name = "My First Model"
        obj_b.my_number = 89
        self.assertEqual("My First Model", obj_b.name)
        self.assertIn("my_number", obj_b.to_dict())

    def test_to_dict(self):
        """Assert expected to_dict() method output."""
        msg = "Unexpected output."""
        obj_b = BaseModel()
        obj_b.id = "74cb9cb3"
        ts = datetime.today()
        obj_b.created_at = ts
        obj_b.updated_at = ts
        ts_iso = ts.isoformat()
        test_dict = {
            "__class__": "BaseModel",
            "id": "74cb9cb3",
            "created_at": ts_iso,
            "updated_at": ts_iso,
        }

        self.assertDictEqual(test_dict, obj_b.to_dict(), msg)

if __name__ == '__main__':
    unittest.main()
