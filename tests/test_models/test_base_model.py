#!/usr/bin/python3
"""
Unit tests for BaseModel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.model = BaseModel()

    def test_id(self):
        """
        Test if id is a string
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """
        Test if created_at is a datetime object
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """
        Test if updated_at is a datetime object
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """
        Test if save method updates updated_at
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(
            model_dict['created_at'], self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'], self.model.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()
