from unittest import TestCase
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt, s = 1, chars[0]
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                cnt += 1
            else:
                if cnt > 1:
                    s += str(cnt)
                s += chars[i]
                cnt = 1
        if cnt > 1:
            s += str(cnt)

        chars[:len(s)] = list(s)
        print(chars)
        return len(s)

class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            (["a","a","b","b","c","c","c"], 6),
            (["a"], 1),
            (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4),
        ]
        for test_case in test_cases:
            answer = self.solution.compress(test_case[0])
            self.assertEqual(answer, test_case[1])
