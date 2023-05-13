#!/usr/bin/python3
"""Unit test suite for Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import time


class TestAmenity(unittest.TestCase):
    """Handles amenity test cases."""

    obj = Amenity()

    def setUp():
        """Prepares test fixtures."""
        pass

    def test_subclass_inheritance(self):
        """Tests if amenity inherits from BaseModel."""
        self.assertIsInstance(self.obj, Amenity)

if __name__ == '__main__':
    unittest.main()
