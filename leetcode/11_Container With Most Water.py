from unittest import TestCase
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) -1
        max_amount = 0

        while i < j:
            if height[i] <= height[j]:
                max_amount = max(max_amount, height[i]*(j-i))
                i += 1
            else:
                max_amount = max(max_amount, height[j] * (j - i))
                j -= 1

        return max_amount


    def timelimit_maxArea(self, height: List[int]) -> int:
        height_i, height_j = 0, 0
        amount = 0
        for i in range(len(height)-1):
            if height[i] < height_i:
                continue
            j = len(height)-1
            while i < j:
                candi_amount = min(height[i], height[j])*(j-i)
                if candi_amount > amount:
                    amount = candi_amount
                    height_i, height_j = height[i], height[j]
                j -= 1

        return amount




class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1),
        ]
        for test_case in test_cases:
            answer = self.solution.maxArea(test_case[0])
            self.assertEqual(answer, test_case[1])
