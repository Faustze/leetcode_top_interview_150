'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # list.insert(index, element)
        for _ in range(k):
            nums.insert(0, nums.pop())


s = Solution()
print(s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))  # -> Output: [5,6,7,1,2,3,4]
print(s.rotate(nums=[-1, -100, 3, 99], k=2))  # -> Output: [3,99,-1,-100]
