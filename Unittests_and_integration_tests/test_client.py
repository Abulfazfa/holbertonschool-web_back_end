#!/usr/bin/env python3
""" Unittests for utils.py
"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_result, mock_get_json):
        # Mock the response of get_json to return the expected result
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the .org property to test
        result = client.org

        # Assert that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the returned result matches the expected result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
