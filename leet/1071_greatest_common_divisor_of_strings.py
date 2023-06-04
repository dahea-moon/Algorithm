from unittest import TestCase

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def _get_gcd(x,y):
            while y:
                x, y = y, x % y

            return x

        if len(str1)==len(str2):
            if str1 == str2:
                return str1
            else:
                return ""

        if len(str1) > len(str2):
            x, y = len(str1), len(str2)
            gcd = _get_gcd(x, y)
        else:
            x, y = len(str2), len(str1)
            gcd = _get_gcd(x, y)

        standard_phrase = str2[:gcd]

        for i in range(len(str1)//gcd):
            if str1[gcd*i:gcd*(i+1)] != standard_phrase:
                return ""

        for i in range(len(str2)//gcd):
            if str2[gcd*i:gcd*(i+1)] != standard_phrase:
                return ""

        return standard_phrase


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            ("ABCDEF", "ABC", "")
        ]
        for test_case in test_cases:
            answer = self.solution.gcdOfStrings(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
