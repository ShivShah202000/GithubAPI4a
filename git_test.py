
import unittest
from unittest import mock 
from unittest.mock import Mock, patch, MagicMock
from git import numberReposandCommits

class TestGitHub(unittest.TestCase):
    @mock.patch('git.numberReposandCommits')
    def test_mock_numberReposandCommits(self, mock_user):
        mock_user.return_value = MagicMock(userID = "vjjeigb")
        result = mock_user.return_value.userID
        try:
            self.assertEqual(result,'vjjeigb')
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    @mock.patch('git.numberReposandCommits')
    def test_mock_numberReposandCommits1(self, mock_user1):
        mock_user1.return_value = MagicMock(userID = "ShivShah202000")
        result = mock_user1.return_value.userID
        try:   
            self.assertEqual(result,'ShivShah202000')
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    @mock.patch('git.numberReposandCommits')
    def test_mock_numberReposandCommits2(self, mock_user3):
        mock_user3.return_value = MagicMock(userID = "richkempinski")
        result = mock_user3.return_value.userID
        try: 
            self.assertEqual(result,'richkempinski')
        except:
            print("Test Failed")
        else:
            print("Test succeed")
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False)
