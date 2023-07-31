class Solution:
    def searchIndex(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if (target == nums[mid]): return mid
            if(target > nums[mid]):
                l = mid + 1
            elif(target < nums[mid]):
                r = mid - 1
        
        return l
    
test = Solution()
print(test.searchIndex([1, 3, 5, 6], 2))