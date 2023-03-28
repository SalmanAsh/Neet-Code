import javax.swing.tree.TreeNode;

public class InvertTree {
    public static void main(String[] args) {
        
    }
    public static TreeNode invertTree(TreeNode root){
        if (root == null){
            return root;
        }
        // TreeNode left = invertTree(root.left);
        // TreeNode right = invertTree(root.right);
        // root.right = left;
        // root.left = right;
        return root;
    }
}
