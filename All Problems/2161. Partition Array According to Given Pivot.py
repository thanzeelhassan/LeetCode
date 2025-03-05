class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:   
        n = len(nums)
        ans = [0] * n
        low_count = 0
        same_count = 0
        high_count = 0
        for i in range(n):
            if nums[i] < pivot:
                low_count += 1
            elif nums[i] > pivot:
                high_count += 1
            else:
                same_count += 1

        low_index = 0
        same_index = 0 + low_count
        high_index = 0 + low_count + same_count

        for i in range(n):
            if nums[i] < pivot:
                ans[low_index] = nums[i]
                low_index += 1
            elif nums[i] > pivot:
                ans[high_index] = nums[i]
                high_index += 1
            else:
                ans[same_index] = nums[i]
                same_index += 1

        return ans
