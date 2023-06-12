from unittest import TestCase
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split()
        a = a[::-1]
        return ' '.join(a)


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ("the sky is blue", "blue is sky the"),
            ("  hello world  ",  "world hello"),
            (" ", ""),
            ("a good   example", "example good a")
        ]
        for test_case in test_cases:
            answer = self.solution.reverseWords(test_case[0])
            self.assertEqual(answer, test_case[1])
