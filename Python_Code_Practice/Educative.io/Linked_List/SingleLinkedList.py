class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #insert at end
    def insert_at_end(self,data):
        new_val = ListNode(data)
        if self.head is None:
            print("List is empty!!")
            self.head = new_val
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_val

    def print(self):
        curr_node = self.head
        sll = ""
        while curr_node:
            sll += str(curr_node.val) + "-->"
            curr_node = curr_node.next
        print(sll)
class Solution:
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(15)
    ll.print()



