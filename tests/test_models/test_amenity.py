#!/usr/bin/python3
"""
Unit tests for Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_attributes(self):
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, 'id'))
        self.assertTrue(hasattr(my_amenity, 'created_at'))
        self.assertTrue(hasattr(my_amenity, 'updated_at'))

    def test_str_method(self):
        my_amenity = Amenity()
        self.assertIsInstance(str(my_amenity), str)

    def test_save_method(self):
        my_amenity = Amenity()
        old_updated_at = my_amenity.updated_at
        my_amenity.save()
        self.assertNotEqual(old_updated_at, my_amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
