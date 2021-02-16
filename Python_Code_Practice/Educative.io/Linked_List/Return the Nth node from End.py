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
        curr_node = head
        count = 0
        while count != n:
            curr_node = curr_node.next
            count += 1
        other = curr_node
        while curr_node:
            curr_node = curr_node.next
            other = other.next
        return other
