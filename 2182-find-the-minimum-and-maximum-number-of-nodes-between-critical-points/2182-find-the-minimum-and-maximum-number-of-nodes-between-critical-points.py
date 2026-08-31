# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        n = 1
        prev_value = 0
        while(head and head.next):
            if(prev_value != 0):
                curr_value = head.val
                next_value = head.next.val
                if ((curr_value < prev_value) and (curr_value < next_value)) or ((curr_value > prev_value) and (curr_value > next_value)):
                    arr.append(n)
            prev_value = head.val
            head = head.next
            n = n + 1

        if len(arr) <= 1:
            return [-1,-1]
                       
        maxDistance = arr[-1] - arr[0]
        minDistance = arr[1] - arr[0]
        n = len(arr)
        for i in range(0,n-1):
            temp = arr[i+1] - arr[i]
            minDistance = min(minDistance, temp)
        
        return [minDistance, maxDistance]