
import unittest
from git import numberReposandCommits

class TestGitHub(unittest.TestCase):

    def testGithub1(self):
        self.assertEqual(numberReposandCommits('vjjeigb'), False)

    def testGithub2(self):
        self.assertEqual(numberReposandCommits('ShivShah202000'), True)
        self.assertEqual(numberReposandCommits('richkempinski'), True)
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
