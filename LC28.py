class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (not needle or needle == haystack): return 0
        needle_len = len(needle)
        
        l = 0
        for r in range(needle_len - 1, len(haystack)):
            if(haystack[l:r + 1] == needle):
                return l
            l += 1
        
        return -1