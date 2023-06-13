from unittest import TestCase
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):
            result[i] = prod
            prod *= nums[i]
        prod = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= prod
            prod *= nums[j]

        return result




class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,2,3,4], [24,12,8,6]),
            ([-1,1,0,-3,3], [0,0,9,0,0])
        ]
        for test_case in test_cases:
            answer = self.solution.productExceptSelf(test_case[0])
            self.assertEqual(answer, test_case[1])
