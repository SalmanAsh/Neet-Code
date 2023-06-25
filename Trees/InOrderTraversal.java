import java.util.Stack;
public class InOrderTraversal {
    public static void main(String[] args) {}
    public static int Kth(TreeNode root, int k){
        int n = 0;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        while(current != null || stack != null){
            while(current != null){
                stack.addElement(current);
                current = current.left;
            }
            current = stack.pop();
            n += 1;
            if(n == k) return current.val;
            current = current.right;
        }
        return -1;
    }
}
