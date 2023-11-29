#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        self.assertIsInstance(str(my_model), str)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
