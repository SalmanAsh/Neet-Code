class Solution1:
    def rep(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        r = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

test = Solution1()
print(test.rep("ABAB", 2))
    

class Solution2:
    def rep(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        r = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if ((r - l + 1) - maxf) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
test = Solution2()
print(test.rep("ABABB", 2))