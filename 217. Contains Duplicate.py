'''Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.'''
import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)


class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        s = Solution()
        self.assertTrue(s.containsDuplicate([1,2,3,1]))
        self.assertFalse(s.containsDuplicate([1,2,3,4]))
        self.assertTrue(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
        self.assertFalse(s.containsDuplicate([]))
        self.assertFalse(s.containsDuplicate([42]))    

if __name__ == '__main__':
    unittest.main()
        