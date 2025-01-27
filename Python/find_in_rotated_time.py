""" Use binary search"""
# pylint: disable:missing-class-docstring,missing-function-docstring
class Solution:
    """ LC 153 """
    def find_min(self, nums: list[int]) -> int:
        """ Solution """
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while  l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = l + ((r - l) // 2)
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res