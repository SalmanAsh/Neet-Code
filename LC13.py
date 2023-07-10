class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        nums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        for i in range(len(s)):
            if i < len(s) - 1 and nums[s[i]] >= nums[s[i+1]]:
                res += nums[s[i]]
            elif i < len(s) - 1 and nums[s[i]] < nums[s[i+1]]:
                res -= nums[s[i]]
            else:
                res += nums[s[i]]
                
        return res


test = Solution()
print(test.romanToInt("III"))