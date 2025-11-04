class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        my_dict = {}
        ans = []
        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] = my_dict[nums[i]] + 1
            else:
                my_dict[nums[i]] = 1
        temp = 0
        count = 0
        highest = 0

        while(count < k):
            for key, value in my_dict.items():
                if value > highest:
                    highest = value
                    temp = key
            ans.append(temp)
            count = count + 1
            highest = 0
            del my_dict[temp]
        return ans 
            