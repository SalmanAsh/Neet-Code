class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        dupl = []
        
        for n in nums:
            if n in seen:
                dupl.append(n)
            else:
                seen.add(n)
        
        return dupl