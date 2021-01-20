# Class definition for Node to be used in Doubly linked List
class DlistNode:
    def __init__(self,val=None,prev=None,next=None):
        self.prev = prev
        self.val = val
        self.next = next

# Create double linked list class
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # insert at begining
    def insert_at_start(self,val):
        new_node = DlistNode(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # print the list
    def print_list(self):
        if self.head is None:
            print("List is empty!!")
            return
        else:
            curr_node = self.head
            list_str = ''
            while curr_node:
                list_str += str(curr_node.val) + "-->"
                curr_node = curr_node.next
            print(list_str)

    # insert at end
    def insert_at_end(self,val):
        if self.head is None:
            print("List is Empty!!!")
            return
        else:
            curr_node = self.head
            new_node = DlistNode(val)
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next=new_node
            new_node.prev = curr_node
            self.tail = new_node

    # Get the size of the linked list, time complexity: O(n)
    def get_length(self):
        if self.head is None:
            print("The List is Empty!!!")
        else:
            size = 0
            curr_node = self.head
            while curr_node:
                size += 1
                curr_node = curr_node.next
            self.tail = curr_node
        return size

    def insert_at(self,ind,value):
        if ind < 0 or ind > self.get_length():
            raise Exception("Invalid Index")

        if ind == 0:
            self.insert_at_begin(value)
            return

        count = 0
        curr_node = self.head
        new_node = DlistNode(value)
        while curr_node:
            if ind-1 == count:
                new_node.next = curr_node.next
                curr_node.next = new_node
                new_node.prev = curr_node
            curr_node = curr_node.next
            count += 1
            self.tail = curr_node
        return

    # remove value at the start in the linked list, time complexity: O(1)

    def remove_at_begin(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    # remove value at the end in the linked list, time complexity: O(n)
    def remove_at_end(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            curr_node.next = None

    # remove at index
    def remove_at_ind(self,ind):
        if ind < 0 or ind > self.get_length():
            raise Exception("Out of Bound")
        if ind == 0:
            self.remove_at_begin()
            return
        if ind == self.get_length():
            self.remove_at_end()
            return
        else:
            curr_node = self.head
            count = 0
            while curr_node:
                if ind-1 == count:
                    curr_node.next.prev = curr_node.prev
                    curr_node.prev.next = curr_node.next
                curr_node = curr_node.next
                count += 1

    #reverse the list
    def reverse_list(self):
        if self.head is None:
            print("Empty list!!")
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            self.tail= curr_node

            rev_curr = self.tail
            rev_str = ''
            while rev_curr:
                rev_str += '<--' + str(rev_curr.val)
                rev_curr = rev_curr.prev
            return rev_str

            


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_start(12)
    dll.insert_at_start(2)
    dll.insert_at_start(20)
    dll.print_list()
    dll.insert_at_end(30)
    dll.print_list()
    print(dll.get_length())
    dll.insert_at(3,80)
    dll.print_list()
    dll.remove_at_begin()
    dll.print_list()
    dll.remove_at_end()
    dll.print_list()
    dll.remove_at_ind(2)
    dll.print_list()
    print(dll.reverse_list())
