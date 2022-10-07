# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:50:07 2022

@author: jay rana
"""

import unittest
from git import numberReposandCommits

class TestGitHub(unittest.TestCase):

    def testGithub1(self):
        self.assertEqual(numberReposandCommits('vjjeigb'), False)

    def testGithub2(self):
        self.assertEqual(numberReposandCommits('ShivShah202000'), True)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
