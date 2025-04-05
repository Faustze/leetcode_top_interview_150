'''Given two strings 's' and 't', return true 
if 't' is an anagram of 's', and false otherwise.'''

import unittest

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        s = Solution()
        self.assertTrue(s.isAnagram("anagram", "nagaram"))
        self.assertFalse(s.isAnagram("rat", "car"))
        self.assertFalse(s.isAnagram("aa", "a"))

if __name__ == '__main__':
    unittest.main()