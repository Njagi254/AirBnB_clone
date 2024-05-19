#!/usr/bin/python3
"""
Unit tests for the console module
"""
import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class
    """
    def setUp(self):
        """Set up test environment"""
        self.backup = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        """Tear down test environment"""
        sys.stdout = self.backup

    def test_quit(self):
        """Test quit command"""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))

    def test_emptyline(self):
        """Test empty line input"""
        console = HBNBCommand()
        console.onecmd("\n")
        self.assertEqual(self.output.getvalue(), "")

    def test_create_missing_class(self):
        """Test create with missing class name"""
        console = HBNBCommand()
        console.onecmd("create")
        self.assertEqual(
            self.output.getvalue().strip(), "** class name missing **"
            )


if __name__ == '__main__':
    unittest.main()
