# Key point:
#   Number of visited nodes should equal n
#   Can't visited something twice -> loop
import collections
class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        prev = -1
        
        def bfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
    
        return dfs(0, -1) and n == len(visited)
            
            
        
        