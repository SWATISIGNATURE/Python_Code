class Solution:
    def min_val(self,lst):
        min_val = float('inf')
        for i in lst:
            if i < min_val:
                min_val = i
        return min_val

lst = [-1,0,1,2,0,9,-2]
print(Solution().min_val(lst))
