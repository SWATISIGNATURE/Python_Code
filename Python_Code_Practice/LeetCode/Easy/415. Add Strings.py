"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library
"""
class Solution:
    def addStrings(self,num1,num2):
        res = []
        carry = 0
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1 >= 0 or p2 >= 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            sum = (n1+n2+carry)%10
            carry = (n1+n2+carry)//10
            res.append(sum)
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(carry)
        return "".join([str(i) for i in res[::-1]])


print(Solution().addStrings('2047','124987'))
