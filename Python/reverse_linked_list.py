# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList1(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
    
    def reorderList2(head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Store all nodes in a list
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Step 2: Reorder the nodes according to the pattern
        i, j = 0, len(nodes) - 1
        while i < j:
            # Link the current node to the node at position j
            nodes[i].next = nodes[j]
            i += 1
            if i == j:  # In case of odd length list
                break
            # Link the node at position j to the node at position i
            nodes[j].next = nodes[i]
            j -= 1
        
        # Step 3: Terminate the list
        nodes[i].next = None