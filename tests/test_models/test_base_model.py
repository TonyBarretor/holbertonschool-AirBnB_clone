#!/usr/bin/python3
"""
Additional unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
import time


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
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertTrue('__class__' in my_model_json)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertTrue('created_at' in my_model_json)
        self.assertTrue('updated_at' in my_model_json)
        self.assertTrue('id' in my_model_json)
        self.assertTrue('name' in my_model_json)
        self.assertTrue('my_number' in my_model_json)

    def test_update_attributes_method(self):
        my_model = BaseModel()
        old_created_at = my_model.created_at
        old_updated_at = my_model.updated_at
        new_attributes = {'name': 'Updated Model', 'my_number': 42}

        for key, value in new_attributes.items():
            setattr(my_model, key, value)

        time.sleep(0.1)

        my_model.save()

        self.assertEqual(old_created_at, my_model.created_at)
        self.assertNotEqual(old_updated_at, my_model.updated_at)
        self.assertEqual(my_model.name, "Updated Model")
        self.assertEqual(my_model.my_number, 42)


if __name__ == '__main__':
    unittest.main()
