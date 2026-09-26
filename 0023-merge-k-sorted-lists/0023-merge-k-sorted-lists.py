# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2 :
            if list1.val < list2.val :
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        if list1 :
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        k = len(lists)
        if k == 0:
            return None
        temp_list = lists[0]
        for i in range(1, k):
            list2 = lists[i]
            temp_list = self.mergeTwoLists(temp_list, list2)

        return temp_list
