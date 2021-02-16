"""Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Accepted
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

class Solution(object):
    def isAnagram(self, s, t):
                """
                :type s: str
                :type t: str
                :rtype: bool
                """
    return collections.Counter(s) == collections.Counter(t)


#OR

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.setdefault(i, 0) + 1
        for i in t:
            if i not in dictionary: return False
            dictionary[i] -= 1
        if dictionary.values() == [0]*len(dictionary): return True
        else: return False



