class Solution:
    def twoSum(self, nums, target):
        val_idx = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in val_idx):
                return [val_idx.get(diff), i]
            val_idx[nums[i]] = i
            

l = [2, 7, 11, 15]
target = 17
test = Solution()
print(test.twoSum(l, target))