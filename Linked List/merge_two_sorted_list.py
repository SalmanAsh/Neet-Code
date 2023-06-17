class Solution:
    def merge(self,  list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while(list1 and list2):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if (not list1):
            tail.next = list2
        elif(not list2):
            tail.next = list1
                
        return dummy.next