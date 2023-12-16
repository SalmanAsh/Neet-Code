class Solution:
    def banners(self, nums, k):
        found = set()
        
        for n in nums:
            if n != 0 and (k/n) in found:
                return (n, int(k/n))
            found.add(n)
        
        return False
    

test = Solution()
print(test.banners([2, 24, 9, 5, 30, 0, 3, 12, 2, 10], 72))
            