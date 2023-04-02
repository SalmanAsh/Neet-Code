class Solution:
    def water(self, height: list[int]) -> int:
        area = 0
        l = 0
        r = 1
        while (l < len(height)-1):
            small = min(height[l], height[r])
            big = max(height[l], height[r])
            a = small * (r - l)
            area = max(a, area)
            if (r == len(height) - 1):
                l += 1
                r = l+1
            elif (r < len(height) - 1):
                r += 1
        return area


test = Solution()
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(test.water(h))


class Solution1:
    def cont(self, height: list[int]) -> int:
        area = 0
        l = 0
        r = len(height)-1
        while (l < r):
            a = min(height[l], height[r]) * (r - l)
            area = max(a, area)
            if (height[l] < height[r]):
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
        return area


test1 = Solution1()
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(test1.cont(h))
