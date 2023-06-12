from unittest import TestCase
from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        vowel_index = [(idx, char) for idx, char in enumerate(s) if char.lower() in vowels]
        j = 0
        for i in range(len(vowel_index)-1, -1, -1):
            vowel_idx = vowel_index[i][0]
            s[vowel_idx] = vowel_index[j][1]
            j += 1

        return ''.join(s)

            
class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ("hello", "holle"),
            ("leetcode","leotcede")
        ]
        for test_case in test_cases:
            answer = self.solution.reverseVowels(test_case[0])
            self.assertEqual(answer, test_case[1])
