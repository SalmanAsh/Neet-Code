#Leetcode 1
# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #val: idx
        mapT = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in mapT:
                return [mapT[temp], i]
            mapT[n] = i