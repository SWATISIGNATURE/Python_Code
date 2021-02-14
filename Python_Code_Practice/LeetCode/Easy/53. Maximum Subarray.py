"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
Input: nums = [1]
Output: 1
Example 3:
Input: nums = [0]
Output: 0
Example 4:
Input: nums = [-1]
Output: -1
Example 5:
Input: nums = [-100000]
Output: -100000
Constraints:
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        else:
            max_val = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] >= max_val:
                        max_val = max(max_val,nums[i] + nums[j])
                    else:
                        break
        return max_val


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))