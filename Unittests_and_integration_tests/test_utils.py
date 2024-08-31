#!/usr/bin/env python3
""" Unittests for utils.py
"""


import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """ TestMemoize class """

    def test_memoize(self):
        """

        Define the class with the memoize decorator

        """
        class TestClass:
            """ TestClass class """
            def a_method(self):
                """ method """
                return 42

            @memoize
            def a_property(self):
                """ decorator """
                return self.a_method()


        # Patch the a_method to observe its behavior when a_property is accessed
        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
