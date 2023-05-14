#!/usr/bin/python3
"""Unit test suite for Place class."""
import unittest
import models
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import time


class TestPlace(unittest.TestCase):
    """Handles place test cases."""
    obj = Place()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_subclass_attributes_exist(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'city_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'description'))
        self.assertTrue(hasattr(self.obj, 'number_rooms'))
        self.assertTrue(hasattr(self.obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.obj, 'max_guest'))
        self.assertTrue(hasattr(self.obj, 'price_by_night'))
        self.assertTrue(hasattr(self.obj, 'latitude'))
        self.assertTrue(hasattr(self.obj, 'longitude'))
        self.assertTrue(hasattr(self.obj, 'amenity_ids'))

    def test_id_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.city_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.description, str)
        self.assertIsInstance(self.obj.number_rooms, int)
        self.assertIsInstance(self.obj.number_bathrooms, int)
        self.assertIsInstance(self.obj.max_guest, int)
        self.assertIsInstance(self.obj.price_by_night, int)
        self.assertIsInstance(self.obj.latitude, float)
        self.assertIsInstance(self.obj.longitude, float)
        self.assertIsInstance(self.obj.amenity_ids, list)
        self.assertIsInstance(self.obj.id, str)
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_inherited_id(self):
        """Assert generated id is unique."""
        obj_p = Place()
        p_obj = Place()
        self.assertNotEqual(obj_p, p_obj)

    def test_save(self):
        """Assert save() method output."""
        obj_p = Place()
        time.sleep(0.12)
        initial_update = obj_p.updated_at
        obj_p.save()
        self.assertLess(initial_update, obj_p.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys."""
        obj_p = Place()
        self.assertIn("__class__", obj_p.to_dict())
        self.assertIn("id", obj_p.to_dict())
        self.assertIn("created_at", obj_p.to_dict())
        self.assertIn("updated_at", obj_p.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values."""
        obj_p = Place()
        obj_p.name = "My First Model"
        obj_p.my_number = 89
        self.assertEqual("My First Model", obj_p.name)
        self.assertIn("my_number", obj_p.to_dict())

    def test_to_dict(self):
        """Assert expected to_dict() method output."""
        msg = "Unexpected output."""
        obj_p = Place()
        obj_p.id = "74cb9cb3"
        ts = datetime.today()
        obj_p.created_at = ts
        obj_p.updated_at = ts
        ts_iso = ts.isoformat()
        test_dict = {
            "__class__": "Place",
            "id": "74cb9cb3",
            "created_at": ts_iso,
            "updated_at": ts_iso,
        }

        self.assertDictEqual(test_dict, obj_p.to_dict(), msg)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(Place(73.756233), BaseModel)
        assert not isinstance(Place(73.756233), float)
        assert not isinstance(b, Place)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        place = Place(73.756233)
        try:
            place.longitude = "longitude type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
