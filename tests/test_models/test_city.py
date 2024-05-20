#!/usr/bin/python3
"""
Unittests for the City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class
    """

    def test_state_id(self):
        """
        Test that the state_id attribute is an empty string
        """
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """
        Test that the name attribute is an empty string
        """
        city = City()
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
