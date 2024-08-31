#!/usr/bin/env python3
""" Unittests for utils.py
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch a_method to observe its behavior when a_property is accessed
        with patch.object(test_instance, 'a_method', return_value=42) as mock_method:
            # Access a_property twice
            first_call = test_instance.a_property
            second_call = test_instance.a_property

            # Assert that the method was called once and result is as expected
            mock_method.assert_called_once()
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)


if __name__ == '__main__':
    unittest.main()

