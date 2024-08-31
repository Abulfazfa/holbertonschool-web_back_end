#!/usr/bin/env python3
""" Unittests for utils.py
"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized

class TestMemoize(unittest.TestCase):
    """ class to test memoize
    """

    def test_memoize(self):
        """ Test memoize
        """
        class TestClass:
            """ Test class
            """

            def a_method(self):
                """a method
                """
                return 42

            @memoize
            def a_property(self):
                """decorator
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
