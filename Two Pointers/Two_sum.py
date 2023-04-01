class Solution:
    def sum(self, numbers: list[int], target: int) -> list[int]:
        idx = []
        l = 0
        r = 1
        while (l <= len(numbers)-2):
            if (numbers[l]+numbers[r] == target):
                idx.append(l+1)
                idx.append(r+1)
                return idx
            elif (numbers[l]+numbers[r] > target):
                l += 1
                r = l+1
            else:
                r += 1


test = Solution()
i = [1, 3, 4, 5, 7, 10, 11]
print(test.sum(i, 9))


class Solution2:
    def sumTwo(self, numbers: list[int], target: int) -> list[int]:
        nums = []
        l = 0
        r = len(numbers)-1
        while (l < r):
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                nums.append(l+1)
                nums.append(r+1)
                return nums


test = Solution2()
i = [1, 3, 4, 5, 7, 10, 11]
print(test.sumTwo(i, 21))
