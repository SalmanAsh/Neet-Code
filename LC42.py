class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_height = [0] * len(height)
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(len(height)):
            if i == 0:
                continue
            else:
                max_left[i] = max(height[:i])
            
            if i == len(height) - 1:
                continue
            else:
                max_right[i] = height[i + 1:]
            
            l = max_left[i]
            r = max_right[i]
            if l >= r:
                diff = r - height[i]
            else:
                diff = l - height[i]
            # mn = min(l, r)
            # min_height[i] = mn
            
            # diff = min_height[i] - height[i]
            if (diff > 0):
                res += diff
        
        return diff

class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while(l < r):
            if leftMax < rightMax:
                l += 1
                res += (leftMax - height[l]) if leftMax - height[l] > 0 else 0
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                res += (rightMax - height[r]) if rightMax - height[r] > 0 else 0
                rightMax = max(rightMax, height[r])
        return res
        
        
            
          