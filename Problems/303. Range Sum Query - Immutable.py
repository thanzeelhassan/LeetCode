class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_array = [0] * (len(nums) +1)
        for i in range(0,len(nums)):
            self.sum_array[i+1] = self.sum_array[i] + nums[i]
    def sumRange(self, left: int, right: int) -> int:
        return self.sum_array[right+1] - self.sum_array[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
