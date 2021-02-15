"""
Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive elements
appear at the other? Solve this problem in Python and see if your code runs correctly!
"""

# class Solution:
#     def rearrange(self,lst):
#         lst.sort()
#         return lst

class Solution:
    def rearrange(self,lst):
        i =-1
        for j in range(len(lst)):
            if lst[j] < 0:
                i += 1
                lst[i],lst[j] = lst[j],lst[i]
                #print(lst)

        return lst



lst = [-11,-1,-2,-3,8,-9,10]
print(Solution().rearrange(lst))