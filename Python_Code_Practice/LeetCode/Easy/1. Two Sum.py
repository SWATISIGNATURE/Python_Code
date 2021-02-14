"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""


class Solution:
    def twoSum(self, nums, target):
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    continue


print(Solution().twoSum([3,2,4],6))
'''
O(N^2)
Optimised :
'''

class solution1:
    def twoSum(self,nums,target):
        result = []
        mymap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff  in mymap:
                result.append(mymap[diff])
                result.append(i)
            else:
                mymap[nums[i]]=i

        return result


print(solution1().twoSum([3, 2, 4], 6))

#OR

class Solution:
    def twoSum(self, nums,target):
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                res.append(i)
                res.append(nums.index(diff))
        return set(res)