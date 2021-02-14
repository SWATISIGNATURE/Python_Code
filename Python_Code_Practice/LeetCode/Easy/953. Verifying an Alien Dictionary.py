"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

class Solution:
    def isAlienSorted(self, words, order):
        dic = {}
        new_words = []
        for i, ch in enumerate(order):
            dic[ch] = i
        #print(dic)
        for w in words:
            new = []
            for c in w:
                new.append(dic[c])
            new_words.append(new)
        #print(new_words)
        for w1, w2 in zip(new_words, new_words[1:]):
            print(w1)
            print(w2)
            if w1 > w2:
                return False
        return True

print(Solution().isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))

l1 = [1,2,3]
l2 = [2,6,9,10]
l3 = [3,5,9,11,45]
l = [l1,l2,l3]
for i,j in zip(l,l[1:]):
    print("here",i,j)

print(Solution().isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))