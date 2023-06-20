from collections import deque
class Solutions:
    #Recursive DFS
    def depth_DFS(self, root: TreeNode) -> int:
        if (not root):
            return 0
        
        return 1 + max(self.depth_DFS(root.left), self.depth_DFS(root.right))
    
    #Breath-First Search
    def depth_BFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                    
            level += 1
        return level
    
    #DFS without recursion
    def depth_iterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 1
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res