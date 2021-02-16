# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # first node
        previous = head
        # second node
        current = head.next

        while current:
            if previous.val == current.val:
                # continue move backwards if previous value is the same as current value
                current = current.next
                # continue point current node
                previous.next = current
            else:
                # move previous to current
                previous = current
                # move current to next
                current = current.next

        return head


