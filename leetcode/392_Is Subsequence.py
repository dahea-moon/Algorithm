from unittest import TestCase
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True if i == len(s) else False


    def isSubsequence_mine(self, s: str, t: str) -> bool:
        n, j = 0, -1
        for i in range(len(s)):
            for k in range(j+1,len(t)):
                if s[i]==t[k]:
                    if k < j:
                        return False
                    j = k
                    n += 1
                    break
            else:
                return False
        else:
            if n == len(s):
                return True
            return False


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ("abc", "ahbgdc", True),
            ("axc",  "ahbgdc", False),
            ("acb", "ahbgdc", False),
            ("aaaaaa", "bbaaaa", False)
        ]
        for test_case in test_cases:
            answer = self.solution.isSubsequence(test_case[0], test_case[1])
            print(answer)
            self.assertEqual(answer, test_case[2])
