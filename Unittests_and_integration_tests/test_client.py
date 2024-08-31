#!/usr/bin/env python3
""" Unittests for utils.py
"""


import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Unit test for GithubOrgClient.public_repos method.
        Mocks get_json and _public_repos_url to ensure proper functionality.
        """
        # Define the payload to be returned by the mocked get_json
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}}
        ]

        # Mock _public_repos_url using patch as a context manager
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "mocked_url"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call public_repos method without license filtering
            repos = client.public_repos()

            # Assert the expected repo list matches the output
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Call public_repos method with license filtering
            repos_with_license = client.public_repos(license="apache-2.0")

            # Assert the expected repo list matches the output when filtering by license
            self.assertEqual(repos_with_license, ["repo1", "repo3"])

            # Assert that _public_repos_url was accessed once and get_json was called once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("mocked_url")


if __name__ == '__main__':
    unittest.main()
