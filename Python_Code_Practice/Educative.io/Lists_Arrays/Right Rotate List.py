"""
Given a list, can you rotate its elements by one index from right to left?
Implement your solution in Python and see if your code runs successfully!
"""

class Solution:
    def right_rotate(self,lst):
        n = len(lst)
        return [lst[-1]]+lst[0:(n-1)]
print(Solution().right_rotate([1,2,3,45,5]))