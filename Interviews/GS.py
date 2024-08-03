class solutions:
    def grid_climbing(self, grid):
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            n = 0
        
        levels = []
        for i in range(m):
            nodes = []
            for j in range(n):
                if grid[i][j] == 1:
                    nodes.append((i, j))
            if nodes:
                levels.append(nodes)
        
        res = 0

        for i in range(len(levels) - 1):
            res += len(levels[i]) * len(levels[i + 1])
        
        return res
    
    def counting_connections(self, matrix):
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            n = 0
        
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        res = 0

        for i in range(m):
            for j in range(n):
                if not matrix[i][j] == 1:
                    continue
                for ni, nj in directions:
                    ni = i + ni
                    nj = j + nj
                    if m > ni >= 0 and n > ni >= 0 and matrix[ni][nj] == 1:
                        res += 1
        return res