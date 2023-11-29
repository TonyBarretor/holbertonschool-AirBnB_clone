#!/usr/bin/python3
"""
Unit tests for Review class
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        my_review = Review()
        self.assertIsInstance(my_review, Review)

    def test_attributes(self):
        my_review = Review()
        self.assertTrue(hasattr(my_review, 'id'))
        self.assertTrue(hasattr(my_review, 'created_at'))
        self.assertTrue(hasattr(my_review, 'updated_at'))

    def test_str_method(self):
        my_review = Review()
        self.assertIsInstance(str(my_review), str)

    def test_save_method(self):
        my_review = Review()
        old_updated_at = my_review.updated_at
        my_review.save()
        self.assertNotEqual(old_updated_at, my_review.updated_at)

    def test_custom_functionality(self):
        my_review = Review()
        # Test custom functionality, for example, a specific method.
        my_review.set_custom_rating(5)
        self.assertEqual(my_review.get_custom_rating(), 5)

    def test_edge_case(self):
        # Test an edge case, for example, handling an empty comment.
        my_review = Review(comment="")
        self.assertEqual(my_review.comment, "")


if __name__ == '__main__':
    unittest.main()
