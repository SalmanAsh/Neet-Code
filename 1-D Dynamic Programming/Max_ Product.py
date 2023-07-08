class Solution:
    # Brute Force attempt
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        for n in range(len(nums)):
            l, r = n, n
            res = max(res, nums[n])
            while(r < len(nums)):
                res = max(res, res * nums[r])
                r += 1
        return res


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        pass
            