# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        curr = head
        while(curr):
            curr = curr.next
            length = length + 1
            # 5
        if length == 1 and n == 1:
            return None
        k = length - n - 1
        # 5 - 2 - 1 = 2
        if k == -1:
            return head.next
        
        curr = head

        while(k > 0):
            k = k - 1
            curr = curr.next

        if curr.next: 
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None

        return head
