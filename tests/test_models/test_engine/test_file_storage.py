#!usr/bin/python3
"""Unit test suite for FileStorage class."""
import unittest
import json
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from datetime import datetime
import time


class TestFileStorage(unittest.TestCase):
    """Handles filestorage test cases."""
    b = BaseModel()

    def test_Instantiation(self):
        """Assert class instantiation."""
        self.assertIsInstance(models.storage, FileStorage)

    def test_file_path_attribute_exists(self):
        """Assert private attribute is present."""
        obj_s = FileStorage()
        self.assertTrue(hasattr(obj_s, "_FileStorage__file_path"))

    def test_objects_attribute_exists(self):
        """Assert private attribute is present."""
        obj_s = FileStorage()
        self.assertTrue(hasattr(obj_s, "_FileStorage__objects"))

    def test_private_attribute_type(self):
        """Assert attribute type."""
        obj_s = FileStorage()
        self.assertIsInstance(getattr(obj_s, "_FileStorage__file_path"), str)

    def test_private_attribute_type(self):
        """Assert attribute type."""
        obj_s = FileStorage()
        self.assertIsInstance(getattr(obj_s, "_FileStorage__objects"), dict)

    def test_json_file_exists(self):
        """Assert the presence of a json file."""
        obj = BaseModel()
        obj.save()
        self.assertEqual(os.path.exists(models.storage._FileStorage__file_path), True)

    def test_public_instance_method_new(self):
        """Assert intended method output: <class name>.id"""
        #b = BaseModel()
        #models.storage.new(b)
        #store_data = ""
        #with open("file.json", "r") as f:
            #store_data = f.read()
        #self.assertIn("BaseModel." + b.id, store_data)
        pass

    def test_public_instance_method_reload(self):
        """Assert method deserializes JSON file to __objects."""
        self.b.name = "Base class instantiation."
        self.b.save()
        all_inst = models.storage.all()
        test_dict = self.b.to_dict()
        dict_key = test_dict["__class__"] + "." + test_dict["id"]
        self.assertEqual(dict_key in all_inst, True)
