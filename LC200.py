import collections
class Solution:
    # Breath First Search
    def numIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    if((r + dr) in range(rows) and (c + dc) in range(cols) and grid[r + dr][c + dc] == 1 and (r + dr, c + dc) not in visited):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands

class Solution:
    # Depth first search
    def numIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def dfs(i, j):
            # Base Case
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == "0" or (i, j) in visited:
                return
            
            visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        
        return res