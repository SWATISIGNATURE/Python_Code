"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        values = []  # O(n) space
        current = head

        # O(n) runtime
        while current:
            values.append(current)
            current = current.next

        if len(values) == 1:
            return None
        else:
            if values[len(values) - n] == head:
                head = head.next
            else:
                values[len(values) - 1 - n].next = values[len(values) - 1 - n].next.next
            return head