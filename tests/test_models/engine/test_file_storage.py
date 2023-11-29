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
        my_storage.save()
        # Agrega pruebas específicas para el método save si es necesario

    def test_new_method(self):
        my_storage = FileStorage()
        # Agrega pruebas específicas para el método new si es necesario

    def test_reload_method(self):
        my_storage = FileStorage()
        # Agrega pruebas específicas para el método reload si es necesario


if __name__ == '__main__':
    unittest.main()
