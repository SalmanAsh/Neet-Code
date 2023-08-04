class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed = ""
        for i in s:
            if(i.isalpha() or i.isdigit()):
                fixed += i
        fixed = fixed.lower()
        l = 0
        r = len(fixed) - 1
        while(l <= r):
           if(fixed[l] != fixed[r]):
               return False
           l += 1
           r -= 1
        return True