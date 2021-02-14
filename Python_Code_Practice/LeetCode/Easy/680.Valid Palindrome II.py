"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution:
    def validPalindrome(self, s):
        for i in range(len(s)):
            temp = s[:i] + s[(i + 1):]
            if temp == temp[::-1]:
                return True
        return s == s[::-1]

print(Solution().validPalindrome("aba"))