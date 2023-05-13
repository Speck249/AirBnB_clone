#!/usr/bin/python3
"""Unit test suite for Review class."""
import unittest
import models
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
import time


class TestReview(unittest.TestCase):
    """Handles review test cases."""
    obj = Review()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(review, BaseModel))

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'place_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'text'))

    def test_id_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.text, str)        
        self.assertIsInstance(self.obj.id, str)
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_inherited_uuid(self):
        """Assert generated id is unique."""
        obj_r = Review()
        r_obj = Review()
        self.assertNotEqual(obj_r, r_obj)

    def test_save(self):
        obj_r = Review()
        time.sleep(0.12)
        initial_update = obj_r.update_at
        obj_r.save()
        self.assertLess(initial_update, obj_r.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys inside dict"""
        obj_r = Review()
        self.assertIn("__class__", obj_r.to_dict())
        self.assertIn("id", obj_r.to_dict())
        self.assertIn("created_at", obj_r.to_dict())
        self.assertIn("updated_at", obj_r.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values within dict."""
        obj_r = Review()
        obj_r.name = "My First Model"
        obj_r.my_number = 89
        self.assertEqual("My First Model", obj_r.name)
        self.assertIn("my_number", obj_r.to_dict())

    def test_to_dict(self):
        """Assert expected method output."""
        msg = "Unexpected output."""
        obj_r = Review()
        ts = datetime.today()
        ts_iso = ts.isoformat()
        obj_r.id = "74cb9cb3-bb94-438b-af2b-7889aef86a8d"
        obj_r.created_at = ts
        obj_r.updated_at = ts
        test_dict = {
            "__class__": "Review",
            "id": "74cb9cb3-bb94-438b-" \
            "af2b-7889aef86a8d",
            "created_at": ts,
            "updated_at": ts,
        }
        self.assertDictEqual(test_dict, obj_r.to_dict(), msg)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(Review("Everything was perfect"), BaseModel)
        assert not isinstance(Review("Everything was perfect"), str)
        assert not isinstance(b, Review)

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
