class ListNode:
    def __init__(self,val=None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_val = ListNode(data)
        if self.head is None:
            self.head = new_val
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_val

    def get_size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

class Solution:
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(12)
    ll.insert_at_end(30)
    #ll.print()
    print(ll.get_size())
