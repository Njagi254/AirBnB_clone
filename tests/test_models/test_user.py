#!/usr/bin/python3
"""
Unittests for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """

    def test_user_attributes(self):
        """
        Test default attributes of User
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
