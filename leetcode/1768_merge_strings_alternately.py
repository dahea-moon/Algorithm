from unittest import TestCase


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for idx in range(min(len(word1), len(word2))):
            result.append(word1[idx])
            result.append(word2[idx])

        if len(word1) > len(result)//2:
            result.append(word1[len(result)//2:])
            return ''.join(result)

        if len(word2) > len(result)//2:
            result.append(word2[len(result)//2:])
            return ''.join(result)

        return ''.join(result)


    def mergeAlternately_one(self, word1: str, word2: str) -> str:
        result = ''
        for char_set in zip(word1, word2):
            result += ''.join(char_set)

        longer_word = word1 if len(word1) > len(word2) else word2
        result += longer_word[len(result)//2:]

        return result


    def mergeAlternately_two(self, word1: str, word2: str) -> str:
        result = ''
        for idx in range(max(len(word1), len(word2))):
            if idx < len(word1):
                result += word1[idx]

            if idx < len(word2):
                result += word2[idx]

        return result


    def mergeAlternately_three(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            return self.mergeAlternately(word1[:len(word2)], word2) + word1[len(word2):]

        if len(word1) < len(word2):
            return self.mergeAlternately(word1, word2[:len(word1)]) + word2[len(word1):]

        result = ''
        for w1, w2 in zip(word1, word2):
            result += w1 + w2

        return result


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ('abc', 'pqr', 'apbqcr'),
            ('ab', 'pqrs', 'apbqrs'),
            ('abcd', 'pq', 'apbqcd')
        ]
        for test_case in test_cases:
            answer = self.solution.mergeAlternately(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
