"""Given a list and a number "k", find two numbers from the list that sum to "k"""

class Solution:
    def find_nums(self,nums,target):
        res = []
        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums and nums.index(val)!= i:
                if nums in res or val in res:
                    continue
                else:
                    res += [nums[i]] + [val]
        return res

nums = [1,2,4,6,5]
target = 6
print(Solution().find_nums(nums,target))








