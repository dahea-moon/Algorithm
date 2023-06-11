from unittest import TestCase
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        greated_candies = max(candies)

        result = [True if i + extra_candies >= greated_candies else False for i in candies]

        return result


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([2,3,5,1,3], 3, [True, True,True,False,True]),
            ([4,2,1,1,2], 1, [True,False,False,False,False]),
            ([12,1,12], 10, [True, False, True]),
        ]
        for test_case in test_cases:
            answer = self.solution.kidsWithCandies(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
