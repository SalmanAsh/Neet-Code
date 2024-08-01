class Solution:
    def permute(self, nums):
        res = []

        def backtrack(curr):
            if(len(curr) == len(nums)):
                res.append(curr.copy())
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
        
        backtrack([])
        return res