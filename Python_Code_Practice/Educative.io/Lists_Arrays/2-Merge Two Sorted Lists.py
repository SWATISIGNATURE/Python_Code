
class Solution:
    def merge_sorted_lists(self,lst1,lst2):
        res = []
        l1 = len(lst1)
        l2 = len(lst2)
        i = 0
        j = 0
        while i < l1 and j < l2:
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i+=1
            else:
                res.append(lst2[j])
                j+=1
        if i < l1:
            res+= lst1[i:]
        if j < l2:
            res+=lst2[j:]

        #OR
        #res = res+lst1[i:]+lst2[j:]

        #OR directly
        #res =sorted(lst1,lst2)
        return res


l1 = [1,2,3,7,10]
l2 = [2,5,6]

print(Solution().merge_sorted_lists(l1,l2))