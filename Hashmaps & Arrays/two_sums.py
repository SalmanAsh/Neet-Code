class Sum:
    """Solution - one"""

    def sum_of_two(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i, j]

        return False


test = Sum()
print(test.sum_of_two([2, 1, 5, 3], 4))
print(test.sum_of_two([2, 7, 11, 15], 9))
print("--------------------")


class Solution:
    """Solution - two"""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val: index
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


test = Solution()
print(test.twoSum([2, 1, 5, 3], 4))
print(test.twoSum([2, 7, 11, 15], 9))
