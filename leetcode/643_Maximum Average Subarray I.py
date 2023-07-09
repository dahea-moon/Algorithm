from unittest import TestCase
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float(-'inf')
        candi_sum = 0
        for i, n in enumerate(nums):
            candi_sum += n
            if i >= k:
                candi_sum -= nums[i-k]

            if i >= k-1:
                max_sum = max(candi_sum, max_sum)

        return max_sum / k


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,12,-5,-6,50,3], 4, 12.75000),
            ([5], 1, 5.00000),
            ([-1], 1, -1)
        ]
        for test_case in test_cases:
            answer = self.solution.findMaxAverage(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
