"""Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself."""

class Solution:
    def product_list(self,lst):
        prod = 1
        for i in lst:
            prod *= i
        res= []
        for i in lst:
            res.append(prod//i)
        return res

#OR
class Solution:
    def product_Array(self,lst):
        def prod(lst):
            prod= 1
            for i in lst:
                prod*=i
            return prod
        res = []
        for i in range(len(lst)):
            res.append(prod(lst[:i])*prod(lst[(i+1):]))
        return res

lst1 = [1,2,3,6,8]
print(Solution().product_list(lst1))
print(Solution().product_Array(lst1))