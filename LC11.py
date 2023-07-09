class Solution:
    # Brute Force solution
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for n in range(len(height)):
            l, r = n, n + 1
            while(r < len(height)):
                base = r - l
                tall = min(height[l], height[r])
                area = max(area, base * tall)
                r += 1
        return area


class Solution:
    # Two Pointers
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        while(l < r):
            base = r - l
            tall = min(height[l], height[r])
            area = max(area, base * tall)
            if(height[l] < height[r]):
                l += 1
            elif(height[r] <= height[l]):
                r -= 1
        return area
