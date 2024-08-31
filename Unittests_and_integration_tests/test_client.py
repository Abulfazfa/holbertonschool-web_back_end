#!/usr/bin/env python3
""" Unit test Test client
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock, call
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    ''' self descriptive '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        ''' self descriptive '''
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """ test that _public_repos_url works """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test the public repos """
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [jeff, bobb, suee]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Jeff', 'Bobb', 'Suee'])
            self.assertEqual(x.public_repos("a"), ['Jeff'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """ test the license checker """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)
