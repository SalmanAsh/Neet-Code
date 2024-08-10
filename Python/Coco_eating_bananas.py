""" KOKO """
import math

class Solution:
    """ Binary Search Solution """
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        """" solution 1"""
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        
        return res
