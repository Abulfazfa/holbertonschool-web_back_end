#!/usr/bin/env python3
""" Unittests for utils.py
"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        # Define the mocked payload for the org property
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result matches the repos_url in the mocked payload
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
