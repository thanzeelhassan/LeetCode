class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = [0] * n

        right_dict = {}
        left_dict = {}
        for i in range(n):
            if nums[i] in right_dict:
                right_dict[nums[i]] += 1
            else:
                right_dict[nums[i]] = 1

        for i in range(0, n):
            if nums[i] in left_dict:
                left_dict[nums[i]] += 1
            else:
                left_dict[nums[i]] = 1

            right_dict[nums[i]] -= 1
            if right_dict[nums[i]] == 0:
                del right_dict[nums[i]]
            
            diff[i] = len(left_dict) - len(right_dict)

        return diff
