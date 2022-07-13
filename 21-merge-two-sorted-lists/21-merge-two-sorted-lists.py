# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None :
            return l2
        if l2 == None:
            return l1
        result = ListNode()
        head = result
        while(l1 != None and l2!= None):
            if l1.val < l2.val:
                result.next = l1
                result = result.next
                l1 = l1.next
            else:
                result.next = l2
                result = result.next
                l2 = l2.next
        if l1!= None:
            result.next = l1
        elif l2 != None:
            result.next = l2
        return head.next