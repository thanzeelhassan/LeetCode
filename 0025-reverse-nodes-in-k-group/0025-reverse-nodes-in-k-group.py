# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # check length of total remaining linked list. if less than n, return 
        n = 0
        curr = head
        while(curr):
            curr = curr.next
            n = n + 1
        if n < k:
            return head

        # find head and tail of the next k nodes
        curr = head
        for _ in range(k-1):
            curr = curr.next
        tail = curr

        next_head = tail.next

        # reverse linked list from head to tail
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next   # SAVE rest of the LL
            curr.next = prev        # FLIP the arrow
            prev = curr             # MOVE prev
            curr = next_node        # MOVE curr

        final_head = prev
        final_tail = head

        # repeat for the next k group
        final_tail.next = self.reverseKGroup(next_head, k)
        
        return final_head
