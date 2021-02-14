"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
            else:
                break
        nums = nums[i:] + nums[:i]
        #print(nums)
        return nums

#OR

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        print(cnt)
        nums[:] = [i for i in nums if i!=0]
        nums += [0]*cnt

print(Solution().moveZeroes([0,1,0,3,12]))
