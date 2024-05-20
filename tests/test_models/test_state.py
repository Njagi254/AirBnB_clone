#!/usr/bin/python3
"""
Unittests for the State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def test_name(self):
        """
        Test that the name attribute is an empty string
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
