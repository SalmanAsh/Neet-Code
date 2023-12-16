class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()
        res = 1
        
        def backtrack(i, j, count, prevNum):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] <= prevNum):
                res = max(res, count)
                return
            
            visited.add((i, j))
            backtrack(i + 1, j, count + 1, matrix[i][j])
            backtrack(i - 1, j, count + 1, matrix[i][j])
            backtrack(i, j + 1, count + 1, matrix[i][j])
            backtrack(i, j - 1, count + 1, matrix[i][j])
            visited.remove((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, 1, None)