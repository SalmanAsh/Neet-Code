class Solution:
    """ Find the largest area in the histogram."""
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """ Solution """
        N = len(heights)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                if i < N - 1 and heights[i] <= heights[j]:
                    res = max(res, heights[i] * j - i + 1)
        
        return res

    def largest_rectangle_area_two(self, heights: list[int]) -> int:
        """ Solution 2"""
        max_area = 0
        stack: list[list[int]] = [] # pair[ind, height]
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area