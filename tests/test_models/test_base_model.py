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

    def test_to_dict_method(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_update_attributes_method(self):
        model = BaseModel()
        old_created, old_updated = model.created_at, model.updated_at

        new_attributes = {
                'created_at': '2023-01-01T00:00:00',
                'custom_attribute': 'custom_value'
        }
        model.update_attributes(new_attributes)

        self.assertNotEqual(old_created, model.created_at)
        self.assertNotEqual(old_updated, model.updated_at)
        self.assertEqual(model.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
