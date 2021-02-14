"""Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: l1 = [], l2 = []
Output: []
Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_curr = l1
        l2_curr = l2

        head = new_curr = ListNode()
        while l1_curr and l2_curr:
            if l1_curr.val < l2_curr.val:
                new_curr.next = l1_curr
                l1_curr = l1_curr.next
                new_curr = new_curr.next
            elif l1_curr.val > l2_curr.val:
                new_curr.next = l2_curr
                l2_curr = l2_curr.next
                new_curr = new_curr.next
            else:
                new_curr.next = l1_curr
                l1_curr = l1_curr.next
                new_curr = new_curr.next
                new_curr.next = l2_curr
                l2_curr = l2_curr.next
                new_curr = new_curr.next
        while l1_curr:
            new_curr.next = l1_curr
            l1_curr = l1_curr.next
            new_curr = new_curr.next

        while l2_curr:
            new_curr.next = l2_curr
            l2_curr = l2_curr.next
            new_curr = new_curr.next

        head = head.next
        return head