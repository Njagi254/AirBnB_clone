#!/usr/bin/python3
"""
Unittests for FileStorage class with User instances
"""

import unittest
from models.engine.file_storage import FileStorage
from models.user import User
import os

class TestFileStorageUser(unittest.TestCase):
    """
    Test cases for FileStorage class with User instances
    """

    def setUp(self):
        """
        Initialize a FileStorage instance before each test
        """
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        # Ensure no file exists before the test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """
        Cleanup after each test
        """
        # Ensure no file remains after the test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_reload_user(self):
        """
        Test save and reload methods with User instances
        """
        user = User()
        user.email = "test@example.com"
        self.storage.new(user)
        self.storage.save()
        
        # Ensure the file is created
        self.assertTrue(os.path.exists(self.file_path))
        
        # Reload storage and check if user instance is restored
        self.storage.reload()
        key = f"User.{user.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].email, "test@example.com")

if __name__ == '__main__':
    unittest.main()