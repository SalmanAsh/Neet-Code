class BruteForce:
    # Brute Force Solution O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for n in range(len(s)):
            l, r = n, n
            temp = 0
            chars = set()
            while r < len(s):
                if s[r] in chars:
                    break
                chars.add(s[r])
                r += 1
                temp += 1
            res = max(res, temp)
        return res

class SlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        chars = set()
        
        while r < len(s):
            while(s[r] in chars):
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
            
            