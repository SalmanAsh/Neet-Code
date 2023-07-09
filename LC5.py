class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        lenString = 0
        for n in range(len(s)):
            
            # Odd length:   b a b a b
            l, r = n, n
            while (l >= 0 and r < len(s) and s [l] == s[r]):
                if (r - l + 1 > lenString):
                    lenString = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
                
            #Even Length:   b a b b a b
            l, r = n, n + 1
            while (l >= 0 and r < len(s) and s [l] == s[r]):
                if (r - l + 1 > lenString):
                    lenString = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res