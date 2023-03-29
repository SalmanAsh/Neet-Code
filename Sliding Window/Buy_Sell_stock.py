class Solution:
    def stock(self, prices: list[int]) -> int:
        l = 0
        r = 1
        profitMax = 0
        while (r < len(prices)):
            if (prices[l] < prices[r]):
                profit = prices[r]-prices[l]
                profitMax = max(profit, profitMax)
            else:
                l = r
            r += 1
        return profitMax


test = Solution()
print(test.stock([7, 8, 1, 9, 2, 10]))
