'''
1. Change the array nums such that the first k elements of nums contain the unique elements 
in the order they were present in nums initially. The remaining elements of nums are not 
important as well as the size of nums.

2. Return k.
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:k]:
                nums[k] = nums[i]
                k += 1
        
        for i in range(k, len(nums)):
            nums[i] = '_'

        return k    

s = Solution()
print(s.removeDuplicates(nums=[1, 1, 2]))  # Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4
# respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
