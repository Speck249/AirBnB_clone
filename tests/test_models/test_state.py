#!/usr/bin/python3
"""Unit test suite for State class."""
import unittest
import models
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
import time


class TestState(unittest.TestCase):
    """Handles state test cases."""
    obj = State()

    def test_subclass_inheritance(self):
        """Assert subclass inheritance from base class."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_id_attribute_exists(self):
        """Assert subclass attributes exist."""
        self.assertTrue(hasattr(self.obj, 'name'))

    def test_id_attribute_exists(self):
        """Assert inherited attribute is present."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_subclass_attribute_type(self):
        """Assert subclass attribute types."""
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.id, str)
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_inherited_id(self):
        """Assert generated id is unique."""
        obj_s = State()
        s_obj = State()
        self.assertNotEqual(obj_s, s_obj)

    def test_save(self):
        """Assert save() method output."""
        obj_s = State()
        time.sleep(0.12)
        initial_update = obj_s.updated_at
        obj_s.save()
        self.assertLess(initial_update, obj_s.updated_at)

    def test_to_dict_keys(self):
        """Assert accuracy of keys."""
        obj_s = State()
        self.assertIn("__class__", obj_s.to_dict())
        self.assertIn("id", obj_s.to_dict())
        self.assertIn("created_at", obj_s.to_dict())
        self.assertIn("updated_at", obj_s.to_dict())

    def test_to_dict_attributes(self):
        """Assert attribute values."""
        obj_s = State()
        obj_s.name = "My First Model"
        obj_s.my_number = 89
        self.assertEqual("My First Model", obj_s.name)
        self.assertIn("my_number", obj_s.to_dict())

    def test_to_dict(self):
        """Assert expected to_dict() method output."""
        msg = "Unexpected output."""
        obj_s = State()
        obj_s.id = "74cb9cb3"
        ts = datetime.today()
        obj_s.created_at = ts
        obj_s.updated_at = ts
        ts_iso = ts.isoformat()
        test_dict = {
            "__class__": "State",
            "id": "74cb9cb3",
            "created_at": ts_iso,
            "updated_at": ts_iso,
        }

        self.assertDictEqual(test_dict, obj_s.to_dict(), msg)

    def test_for_polymorphism(self):
        """Assert interchangeability between base & subclass."""
        b =  BaseModel()
        assert isinstance(State("New York"), BaseModel)
        assert not isinstance(State("New York"), str)
        assert not isinstance(b, State)

    def test_subclass_exceptions(self):
        """Assert exception handling."""
        state = State("New York")
        try:
            state.name = "name type error"
        except Exception as e:
            assert isinstance(e, TypeError)

if __name__ == '__main__':
    unittest.main()
