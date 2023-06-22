from collections import deque
#Breath First Search Algorithm
class Solution:
    def level_traversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        q = deque([root])
        res = []
        
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if(node):
                    tmp.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if(level):
               res.append(tmp)
        return res