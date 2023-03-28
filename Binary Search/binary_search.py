class BinarySearch:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                return mid
        return -1


test = BinarySearch()
l = [1, 2, 3, 4, 5, 6, 7]
print(test.search(l, 2))

l = [-2, -1, 2, 6, 8, 10]
print(test.search(l, 8))
