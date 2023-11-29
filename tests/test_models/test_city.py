#!/usr/bin/python3
"""
Unit tests for City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, 'id'))
        self.assertTrue(hasattr(my_city, 'created_at'))
        self.assertTrue(hasattr(my_city, 'updated_at'))

    def test_str_method(self):
        my_city = City()
        self.assertIsInstance(str(my_city), str)

    def test_save_method(self):
        my_city = City()
        old_updated_at = my_city.updated_at
        my_city.save()
        self.assertNotEqual(old_updated_at, my_city.updated_at)

    def test_custom_functionality(self):
        my_city = City()
        # Test custom functionality, for example, a specific method.
        my_city.set_custom_property("Custom Value")
        self.assertEqual(my_city.get_custom_property(), "Custom Value")

    def test_edge_case(self):
        # Test an edge case, for example, handling an empty name.
        my_city = City(name="")
        self.assertEqual(my_city.name, "")


if __name__ == '__main__':
    unittest.main()
