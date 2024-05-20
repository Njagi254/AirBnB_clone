#!/usr/bin/python3
"""
Unittests for the Review class
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
    """

    def test_place_id(self):
        """
        Test that the place_id attribute is an empty string
        """
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """
        Test that the user_id attribute is an empty string
        """
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text(self):
        """
        Test that the text attribute is an empty string
        """
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
