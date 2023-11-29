#!/usr/bin/python3
"""
Unit tests for Place class
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_instance_creation(self):
        my_place = Place()
        self.assertIsInstance(my_place, Place)

    def test_attributes(self):
        my_place = Place()
        self.assertTrue(hasattr(my_place, 'id'))
        self.assertTrue(hasattr(my_place, 'created_at'))
        self.assertTrue(hasattr(my_place, 'updated_at'))

    def test_str_method(self):
        my_place = Place()
        self.assertIsInstance(str(my_place), str)

    def test_save_method(self):
        my_place = Place()
        old_updated_at = my_place.updated_at
        my_place.save()
        self.assertNotEqual(old_updated_at, my_place.updated_at)


if __name__ == '__main__':
    unittest.main()
