class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        middle = (left + right) // 2
        while(left < right):
            middle = (left + right) // 2
            #print(left,right,middle)
            if left + 1 == right :
                if left == 0:
                    if nums[right] == nums[right + 1]:
                        return nums[left]
                    else:
                        return nums[right]
                elif right == n - 1 :
                    if nums[left] == nums[left - 1]:
                        return nums[right]
                    else:
                        return nums[left]
                elif nums[left] == nums[left - 1]:
                    return nums[right]
                else:
                    return nums[left]

            if middle % 2 == 0:
                if nums[middle] == nums[middle - 1] :
                    right = middle - 1
                else:
                    left = middle
            else:
                if nums[middle] == nums[middle - 1]:
                    left = middle + 1
                else:
                    right = middle
        middle = (left + right) // 2
        #print(left,right,middle)
        return nums[middle]
