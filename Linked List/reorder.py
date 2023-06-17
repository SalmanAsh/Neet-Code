class Solution:
    def reorder(self, head: ListNode) -> None:
        #divide the list in two
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fats = fast.next.next
        
        second = slow.next
        slow.next = None
        
        #Reverse second list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        
        
        #Merge the two lists
        second = prev
        first = head
        while (second):
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2