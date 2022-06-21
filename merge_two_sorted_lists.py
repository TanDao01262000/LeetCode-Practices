# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            return list2
        elif list2:
            return list1    
        else:
            if list1.val < list2.val:
                res = ListNode(list1.val)
                res.next = self.mergeTwoLists(list1.next, list2)
            else:
                res = ListNode(list2.val)
                res.next = self.mergeTwoLists(list1, list2.next)
        return res