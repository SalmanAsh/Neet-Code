public class Reverse {
    public static void main(String args[]){

    }
    public static <ListNode> ListNode rev(ListNode head){
        ListNode prev = null;

        while (head != null){
            // ListNode next_node = head.next;
            // head.next = prev;
            prev = head;
            // head = next_node;
        }
        return prev;
    }
}
