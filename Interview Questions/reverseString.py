class Solution:
    def revString(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        return s[-1] + str(self.revString(s[:-1]))

test = Solution()
print(test.revString("hello"))