class Solution:
    def reverseList(self, head):

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def reverseList_recursive(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return newHead