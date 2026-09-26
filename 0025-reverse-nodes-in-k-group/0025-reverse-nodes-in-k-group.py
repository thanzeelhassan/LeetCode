# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findHeadandTailofNextKGroup(self, head, k):
        # find head and tail of the next k nodes
        curr = head
        while(k > 1):
            curr = curr.next
            k = k - 1
        tail = curr
        return head, tail

    def reverseNextKGroup(self, head, k):
        # reverse linked list from head to tail
        prev = None
        curr = head

        while (k > 0):
            next_node = curr.next   # SAVE rest of the LL
            curr.next = prev        # FLIP the arrow
            prev = curr             # MOVE prev
            curr = next_node        # MOVE curr
            k = k - 1

        return prev, head

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # find head and tail of the first k nodes
        # reverse these k nodes
        # join them with the rest
        # repeat for rest of the nodes

        # check length of total remaining linked list
        n = 0
        curr = head
        while(curr):
            curr = curr.next
            n = n + 1
        if n < k:
            return head
        else:
            head_backup = head
            head, tail = self.findHeadandTailofNextKGroup(head, k)
            next_head = tail.next
            final_head, final_tail = self.reverseNextKGroup(head, k)
            final_tail.next = self.reverseKGroup(next_head, k)
        
        return final_head
