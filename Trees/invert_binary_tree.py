class solution:
    def tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.tree(root.left)
        self.tree(root.right)
        return root
