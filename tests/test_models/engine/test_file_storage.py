#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_instance_creation(self):
        my_storage = FileStorage()
        self.assertIsInstance(my_storage, FileStorage)

    def test_save_method(self):
        my_storage = FileStorage()
        # Add specific tests for the save method if needed
        pass

    def test_custom_functionality(self):
        my_storage = FileStorage()
        my_storage.set_custom_config("Custom Value")
        self.assertEqual(my_storage.get_custom_config(), "Custom Value")

    def test_edge_case(self):
        # Test an edge case, for example, handling an empty data input.
        my_storage = FileStorage()
        self.assertEqual(my_storage.data, None)

    def test_new_method(self):
        my_storage = FileStorage()
        # Add specific tests for the new method if needed
        pass

    def test_reload_method(self):
        my_storage = FileStorage()
        # Add specific tests for the reload method if needed
        pass

    def test_set_get_data_methods(self):
        my_storage = FileStorage()
        my_data = {'key': 'value'}
        my_storage.set_data(my_data)
        self.assertEqual(my_storage.get_data(), my_data)


if __name__ == '__main__':
    unittest.main()
