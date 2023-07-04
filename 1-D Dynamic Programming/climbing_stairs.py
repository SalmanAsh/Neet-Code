class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for i in range(n - 1):
            tmp = two
            one = one + two
            two = tmp
        return one