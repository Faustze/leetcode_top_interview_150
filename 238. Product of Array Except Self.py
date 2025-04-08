'''Given an integer array 'nums', return an array 'answer' such that answer[i] is equal to
the product of all the elements of 'nums' except nums[i].'''
import unittest

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer


class TestSolution(unittest.TestCase):
    def test_productExceptSelf(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(s.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
        self.assertEqual(s.productExceptSelf([]), [])


if __name__ == '__main__':
    unittest.main()