from unittest import TestCase
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                # tracking zero index
                j += 1

        return nums




class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([0,1,3,0,12], [1,3,12,0,0]),
            ([0], [0])
        ]
        for test_case in test_cases:
            answer = self.solution.moveZeroes(test_case[0])
            self.assertEqual(answer, test_case[1])
