class Solution:
    def permutations(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        if len(nums) == 1:
            return[nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            permute = self.permutations(nums)
            
            for perm in permute:
                perm.append(n)
            
            res.extend(permute)
            nums.append(n)
        return res