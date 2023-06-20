#My Solution
class Solution:
    def same(self, p: TreeNode, q: TreeNode) -> bool:
        if(not p and not q):
            return True
        
        if(not p or not q):
            return False
        
        if(p.val == q.val):
            return True and self.same(p.left, q.left) and self.same(p.right, q.right)
        
        return False