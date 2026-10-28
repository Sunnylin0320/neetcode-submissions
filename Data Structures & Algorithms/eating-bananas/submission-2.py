import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        else:
            l, r = 1, max(piles)
            while l < r:
                k = (l + r) // 2
                hours = 0
                for p in piles:
                    hours += math.ceil(p / k)
                if hours <= h:
                    r = k
                else:
                    l = k + 1
            return l

