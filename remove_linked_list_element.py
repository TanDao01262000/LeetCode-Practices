# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #  Solution 1: using 2 pointer for keep tracking pre and cur, O(n) time and O(1) space
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
            
        return dummy.next
            
    # Solution 2: using 1 cur pointer and while loop to check cur.next val instead of check cur.val     
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if head:    
            cur = head
            while cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        return head


            
                    
            