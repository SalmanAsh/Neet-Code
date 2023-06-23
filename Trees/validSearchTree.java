import javax.swing.tree.TreeNode;

public class validSearchTree{
    public static void main(String[] args) {    
    }
    public static boolean isValidBST(TreeNode root){
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public static boolean isValidBST(TreeNode root, long minValue, long maxValue){
        if(root == null) return true;
        // if(!(root.val > minValue && root.val < maxValue)) return false;
        // return isValidBST(root.left, minValue, root.val) && isValidBST(root.right, root.val, maxValue);
        return false;
    }
}