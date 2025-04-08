'''Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.'''
import unittest

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_of_top = {}
        
        for num in nums:
            data_of_top[num] = data_of_top.get(num, 0) + 1 
            
        sorted_elements = sorted(data_of_top.keys(), key=lambda x: -data_of_top[x])
        return sorted_elements[:k]



class TestSolution(unittest.TestCase):
    def test_topKFrequent(self):
        s = Solution()
        self.assertEqual(s.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(s.topKFrequent([1], 1), [1])
        self.assertEqual(s.topKFrequent([3, 0, 1, 0], 1), [0])

if __name__ == '__main__':
    unittest.main()