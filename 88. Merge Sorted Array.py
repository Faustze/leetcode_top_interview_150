'''
1. Объединить nums1 и nums2 в один неубывающий массив;
2. len(nums1) = m + n;
3. Первые m элементов должны быть объеденены, а последние n элементов представленны в виде 0;
4. len(nums2) = n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: Массивы, которые мы объединяем, это [1,2,3] и [2,5,6].
Результатом слияния является [1,2,2,3,5,6] с подчеркнутыми элементами, взятыми из nums1.
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()