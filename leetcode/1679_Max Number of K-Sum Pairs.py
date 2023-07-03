from unittest import TestCase
from typing import List

class Solution:
    # using hash table
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_table = {}
        cnt = 0
        for num in nums:
            if k - num in hash_table and hash_table[k-num] > 0:
                cnt += 1
                hash_table[k-num] -= 1
            elif num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1

        return cnt


    # two pointers
    def OnemaxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i, j = 0, len(nums)-1
        while i < j:
            n = nums[i] + nums[j]
            if n == k:
                cnt += 1
                i += 1
                j -= 1
            elif n > k:
                j -= 1
            else:
                i += 1

        return cnt

class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,2,3,4], 5, 2),
            ([3,1,3,4,3], 6, 1),
            ([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2, 2)
        ]
        for test_case in test_cases:
            answer = self.solution.maxOperations(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
