class ListNode:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.nxt = nxt
#Iteration solution
class Solution:
    def rev(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            nxt = current.next
            current.next = prev
            pre = current
            current = nxt
        return prev







#recursive
class Solution2:
    def lnkdldt(self, head: ListNode) -> ListNode:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.lnkdldt(head.next)
            head.next.next = head
        head.next = None
        
        return newHead