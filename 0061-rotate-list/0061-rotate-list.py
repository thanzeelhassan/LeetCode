# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # if the linked list in None
        if not head : 
            return None
        # if the linked list is just one value :
        if not head.next :
            return head
        if k == 0:
            return head

        n = 0
        curr = head
        while(curr):
            temp = curr
            curr = curr.next
            n = n + 1

        tail = temp

        k = k % n
        if k == 0:
            return head
        t = n - k

        curr = head
        for i in range(0, t-1):
            curr = curr.next

        temp = curr.next
        curr.next = None
        tail.next = head
        head = temp

        return head
