'''Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.'''
import unittest

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
            
        return list(anagram_groups.values())

            
class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        s = Solution()
        self.assertEqual(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), 
                         [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(s.groupAnagrams([""]), [[""]])
        self.assertEqual(s.groupAnagrams(["a"]), [["a"]])
        # self.assertEqual(s.groupAnagrams()

if __name__ == '__main__':
    unittest.main()