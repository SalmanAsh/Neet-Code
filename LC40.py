class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(pos, cur, total):
            if (total == target):
                res.append(cur.copy())
                return
            if(pos >= len(candidates) or total > target):
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if (candidates[i] == prev):
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
                prev = candidates[i]
                
        dfs(0, [], 0)
        return res