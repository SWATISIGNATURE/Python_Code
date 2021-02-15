class Solution:
    def remove_even(self,lst):
        res = []
        for i in lst:
            if i%2 == 0:
                continue
            else:
                res.append(i)
        return res

    def remove_even_inplace(self,lst):
        lst = [i for i in lst if i%2 != 0]
        return lst

lst = [0,1,2,6,9]
print(Solution().remove_even(lst))
print(Solution().remove_even_inplace(lst))
