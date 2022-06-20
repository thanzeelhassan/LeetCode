class Solution(object):
    def reorderList(self, head):
        if head.next:
            # step 1: find the middle pointer of the linked list
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None

            # step 2: reverse the last half linked list
            p, q, mid.next = mid, mid.next, None
            while q:
                p, q, p.next = q, q.next, p
            mid = p

            # step 3: merge first half and reversed last half
            p, q = head, mid
            while q:
                pp, qq = p, q  # backup p and q
                p, q = p.next, q.next
                pp.next, qq.next = qq, p
