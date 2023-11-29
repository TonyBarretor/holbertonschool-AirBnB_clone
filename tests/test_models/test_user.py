#!/usr/bin/python3
"""
Unit tests for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_instance_creation(self):
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_attributes(self):
        my_user = User()
        self.assertTrue(hasattr(my_user, 'id'))
        self.assertTrue(hasattr(my_user, 'created_at'))
        self.assertTrue(hasattr(my_user, 'updated_at'))

    def test_str_method(self):
        my_user = User()
        self.assertIsInstance(str(my_user), str)

    def test_save_method(self):
        my_user = User()
        old_updated_at = my_user.updated_at
        my_user.save()
        self.assertNotEqual(old_updated_at, my_user.updated_at)


if __name__ == '__main__':
    unittest.main()
