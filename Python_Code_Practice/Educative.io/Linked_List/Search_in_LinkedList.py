class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_val = ListNode(data)
        if self.head is None:
            self.head = new_val
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_val

    def print(self):
        if self.head is None:
            return None
        else:
            curr_node = self.head
            sll = ''
            while curr_node:
                sll += str(curr_node.val) + "-->"
                curr_node = curr_node.next
            print(sll)

    def search_val(self,data):
        if self.head is None:
            return None
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.val == data:
                    return True
                curr_node = curr_node.next
            return False

class Solution:
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(15)
    ll.insert_at_end(32)
    ll.print()
    print(ll.search_val(11))
    print(ll.search_val(15))



