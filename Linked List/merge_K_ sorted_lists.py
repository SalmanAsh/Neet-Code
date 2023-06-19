class Solution:
    def merge(self, lists: List[ListNode]) -> ListNode:
        if (not lists or len(lists) == 0):
            return None
        
        while(len(lists) > 1):
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge2list(l1, l2))
            lists = mergedLists
        
        return lists[0]
    
    
    def merge2list(self,  list1: ListNode, list2: ListNode) -> Optional[ListNode]:
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