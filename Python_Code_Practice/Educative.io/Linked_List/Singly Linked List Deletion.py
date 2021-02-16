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
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_val

    def print(self):
        if self.head is None:
            return None
        else:
            sll = ""
            curr_node = self.head
            while curr_node:
                sll += str(curr_node.val) + "-->"
                curr_node = curr_node.next
        print(sll)

    def delete_val(self,data):
        if self.head is None:
            return None
        elif self.head.val == data:
            self.head = self.head.next
        else:
            curr_node = self.head
            while curr_node.next:
                if curr_node.next.val == data:
                    curr_node.next = curr_node.next.next
                    print("deleted")
                else:
                    curr_node = curr_node.next


class Solution:
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(15)
    ll.print()
    ll.delete_val(12)
    ll.delete_val(20)
    ll.print()