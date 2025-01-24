'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1: Input: nums = [3,2,3] Output: 3 
Example 2: Input: nums = [2,2,1,1,1,2,2] Output: 2
'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = None
        for num in set(nums):
            if nums.count(num) > n / 2:
                majority_element = num

        return majority_element


s = Solution()
print(s.majorityElement(nums=[3, 2, 3]))
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
