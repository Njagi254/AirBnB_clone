#!/usr/bin/python3
"""
Unit tests for BaseModel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.model = BaseModel()
        self.model.name = "My_First_Model"
        self.model.my_number = 89

    def test_base_model(self):
        """
        Test creating, saving, and to_dict of a BaseModel instance
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'My_First_Model')
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(
            model_dict['created_at'], self.model.created_at.isoformat()
            )
        self.assertEqual(
            model_dict['updated_at'], self.model.updated_at.isoformat()
            )

        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_save(self):
        """
        Test if save method updates updated_at
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
