from unittest import TestCase
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # i = smallest, j = second_smallest
        i = j = float('inf')
        for n in range(len(nums)):
            if nums[n] < i:
                i = nums[n]
            elif i < nums[n] < j:
                j = nums[n]
            elif nums[n] > j:
                return True

        return False

class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,2,3,4,5], True),
            ([5,4,3,2,1], False),
            ([2,1,5,0,4,6], True),
            ([20,100,10,12,5,13], True)
        ]
        for test_case in test_cases:
            answer = self.solution.increasingTriplet(test_case[0])
            self.assertEqual(answer, test_case[1])
