"""Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on."""

class Solution:
    def min_max_form(self,lst):
        res = []
        for i in range(len(lst)//2):
            res.append(lst[-(i+1)])
            res.append(lst[i])
        if len(lst)%2!=0:
            res = res + [lst[i+1]]
        return res


lst = [1,2,4,6,8,10,19]
print(Solution().min_max_form(lst))


