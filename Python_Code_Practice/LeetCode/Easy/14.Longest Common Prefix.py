"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        i=0
        if strs:
            while i < len(strs[0]):
                if strs[0][i] == strs[-1][i]:
                    i+=1
                else:
                    break

        else:
            return ""
        return strs[0][:i]

print(Solution().longestCommonPrefix([""]))