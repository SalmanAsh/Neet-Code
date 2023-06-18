#Check if there is a cycle in the linked list
#my solution
class Solution:
    def cycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while True:
            if (not fast or not fast.next):
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if (slow == fast):
                return True


class Solution2:
    def cycle(self, head: ListNode) -> bool:
        slow = head = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False