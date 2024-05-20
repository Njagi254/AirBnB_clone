#!/usr/bin/python3
"""
Unittests for the Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """

    def test_name(self):
        """
        Test that the name attribute is an empty string
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
