"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
Example:
Input:
[1,2,3]
Output:
3
Explanation:
Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

class Solution:
    def minMoves(self, nums):
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return abs(nums[0]-nums[1])
        else:
            count = 0
            while True:
                max_val = max(nums)
                min_val = min(nums)
                if max_val == min_val:
                    break
                idx = nums.index(max_val)
                print(idx,max_val)
                count += 1
                for i in range(len(nums)):
                    if i != idx:
                        nums[i] += 1
                    print(nums)


        return count

#OR

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == nums[0]:
                break
            else:
                count += nums[i] - nums[0]
        return count


print(Solution().minMoves([1,2,3]))