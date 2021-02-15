"""
Given a list, find the first integer which is unique in the list.
Unique means the number does not repeat and appears only once in the whole list.
 Implement your solution in Python and see if it runs correctly!
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        my_map = Counter(s)
        # print(my_map)
        for i, v in enumerate(s):
            if my_map[v] == 1:
                return v

lst = [1,2,1,3,4,5,6,6,4]
print(Solution().firstUniqChar(lst))