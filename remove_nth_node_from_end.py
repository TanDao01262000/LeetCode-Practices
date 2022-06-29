# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #  SOlution 1: dividing into three cases:
    #  1 - only one node, 2 - delete the head node, 3 - delete non-head node
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        #  Case 1: set the head to none right the way
        if length == 1:
            head = None
        else:
            # when there are more than 1 node
            prev = ListNode(next=None)    
            cur = head
            for _ in range(length-n-1):
                cur = cur.next
            # wanna delete the head
            if cur == head and n == length:
                prev.next = head.next
                head = prev.next
            else:
            # delete other nodes 
                cur.next = cur.next.next
        return head
