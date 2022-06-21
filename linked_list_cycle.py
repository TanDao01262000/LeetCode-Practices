# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst   = {}
        
        while head:
            if head.next in lst:
                return True
            lst[head] = True
            head = head.next
        
        return False
