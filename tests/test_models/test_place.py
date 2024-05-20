#!/usr/bin/python3
"""
Unittests for the Place class
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class
    """

    def test_city_id(self):
        """
        Test that the city_id attribute is an empty string
        """
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """
        Test that the user_id attribute is an empty string
        """
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """
        Test that the name attribute is an empty string
        """
        place = Place()
        self.assertEqual(place.name, "")

    def test_description(self):
        """
        Test that the description attribute is an empty string
        """
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """
        Test that the number_rooms attribute is 0
        """
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        Test that the number_bathrooms attribute is 0
        """
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test that the max_guest attribute is 0
        """
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """
        Test that the price_by_night attribute is 0
        """
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        """
        Test that the latitude attribute is 0.0
        """
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """
        Test that the longitude attribute is 0.0
        """
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        Test that the amenity_ids attribute is an empty list
        """
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
