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

    def test_custom_functionality(self):
        my_amenity = Amenity()
        # Test custom functionality, for example, a specific method.
        my_amenity.set_custom_property("Custom Value")
        self.assertEqual(my_amenity.get_custom_property(), "Custom Value")

    def test_edge_case(self):
        # Test an edge case, for example, handling an empty name.
        my_amenity = Amenity(name="")
        self.assertEqual(my_amenity.name, "")


if __name__ == '__main__':
    unittest.main()
