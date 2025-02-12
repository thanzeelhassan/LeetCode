class Solution:
    def maximumSum(self, nums: List[int]) -> int:
            my_dict = {}
            n = len(nums)

            ans = -1

            for i in range(n):
                s = nums[i]
                sum_ = 0
                while(s > 0):
                    last = s % 10
                    s = int(s / 10)
                    sum_ = sum_ + last

                if sum_ in my_dict: 
                    if len(my_dict[sum_]) == 1:
                        if nums[i] > my_dict[sum_][0]:
                            my_dict[sum_].append(nums[i]) 
                        else:
                            temp = my_dict[sum_][0]
                            my_dict[sum_] = [nums[i], temp]
                        temp = sum(my_dict[sum_])
                        if temp > ans :
                            ans = temp
                    else:
                        arr = my_dict[sum_]
                        a, b = arr[0], arr[1]
                        if nums[i] > a:
                            if nums[i] > b :
                                temp = my_dict[sum_][1]
                                my_dict[sum_] = [temp, nums[i]]
                            else:
                                temp = my_dict[sum_][1]
                                my_dict[sum_] = [nums[i], temp]
                            temp = sum(my_dict[sum_])
                            if temp > ans :
                                ans = temp
                else:
                    my_dict[sum_] = [nums[i]]

            return ans