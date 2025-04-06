'''Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. You may assume that each input would 
have exactly one solution, and you may not use the same element twice.
You can return the answer in any order'''
import unittest

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(s.twoSum([3, 3], 6), [0, 1])
        self.assertEqual(s.twoSum([3, 2, 3], 6), [0, 2])

if __name__ == '__main__':
    unittest.main()