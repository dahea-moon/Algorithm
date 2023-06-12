from unittest import TestCase
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        idx = 0
        planted = 0
        for i in range(n):
            while idx < len(flowerbed):
                if flowerbed[idx]:
                    idx += 1
                elif not flowerbed[idx]:
                    if idx == len(flowerbed)-1 and not flowerbed[idx-1]:
                        flowerbed[idx] = 1
                        planted += 1
                        break
                    elif idx == 0 and not flowerbed[idx+1]:
                        flowerbed[idx] = 1
                        planted += 1
                        break
                    elif not flowerbed[idx-1] and not flowerbed[idx+1]:
                        flowerbed[idx] = 1
                        planted += 1
                        break
                    else:
                        idx += 1

        if planted == n:
            return True

        return False


    def fastest(self, flowerbed: List[int], n: int) -> bool:
        cnt, beds = 1, 0

        for bed in flowerbed:
            if bed:
                cnt = 0
            else:
                cnt += 1
                if cnt == 3:
                    cnt = 1
                    beds += 1

        if not flowerbed[-1]:
            cnt += 1
            if cnt == 3:
                beds += 1
        return beds >= n


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_testcases(self):
        test_cases = [
            ([1,0,0,0,1], 1, True),
            ([1,0,0,0,1], 2, False),
            ([1,0,1,0,1,0,1], 1, False)
        ]
        for test_case in test_cases:
            answer = self.solution.canPlaceFlowers(test_case[0], test_case[1])
            self.assertEqual(answer, test_case[2])
