class Solution:
    def ones(self, n: int) -> int:
        count = 0
        while (n > 0):
            count += n % 2
            n = n >> 1
        return count


test = Solution()
print(test.ones(100100100111))


class Solution1:
    def bits(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count


test = Solution1()
print(test.bits(100100100111))
