class Solution:
    # Backtracking solution
    def generateParanthesis(self, n: int) -> List[str]:
        arr = []
        
        def backtrack(current_str, opn, close, mx):
            if (len(current_str) == mx * 2):
                arr.append(current_str)
                return
            
            if (opn < mx): backtrack(current_str + "(", opn + 1, close, mx)
            if (close < opn): backtrack(current_str + ")", opn, close + 1, mx)
            
        backtrack("", 0, 0, n)
        return arr

class Solution2:
    # Stack solution
    def generateParanthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if (openN == closedN == n):
                res.append("".join(stack))
                return
            
            if (openN < n):
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if (closedN < openN):
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res