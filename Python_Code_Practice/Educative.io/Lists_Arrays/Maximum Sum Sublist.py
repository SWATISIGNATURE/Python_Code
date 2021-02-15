"""Given an array, find the contiguous sublist with the largest sum."""

class Solution:
    def max_subarray(self,nums):
        curr_max = nums[0]
        max_val = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i],curr_max+nums[i])
            max_val = max(max_val,curr_max)
        return max_val


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().max_subarray(nums))