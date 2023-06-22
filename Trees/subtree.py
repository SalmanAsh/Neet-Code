class Solution:
    #my solution
    def isSubtree(self, root: TreeNode, subroot: TreeNode) -> bool:
        if (not root and not subroot):
            return True
        if (not root and subroot):
            return False
        if(root and not subroot):
            return True
        
        if self.isSame(root, subroot):
            return True
    
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
    
    def isSame(self, p: TreeNode, q: TreeNode) -> bool:
        if(not p and not q):
            return True
        
        if(not p or not q):
            return False
        
        if(p.val == q.val):
            return True and self.same(p.left, q.left) and self.same(p.right, q.right)
        
        return False