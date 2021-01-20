# Definition of Node class for Linked List
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Definition of Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # insert at the beginning, time complexity: O(n)
    def insert_at_begin(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at end, time complexity: O(n)
    def insert_at_end(self,val):
        new_node = ListNode(val)
        if self.head is None:
            print("The list is empty!!!")
            self.head = new_node
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    # insert multiple values in the linked list, time complexity: O(n)
    def insert_multiple(self,add_list):
        for each in add_list:
            self.insert_at_end(each)

    # insert value at the given index in the linked list, time complexity: O(n)
    def insert_at(self,ind,value):
        if ind < 0 or ind > self.get_length():
            raise Exception("Invalid Index")

        if ind == 0:
            self.insert_at_begin(value)
            return

        count = 0
        curr_node = self.head
        new_node = ListNode(value)
        while curr_node:
            if ind-1 == count:
                new_node.next = curr_node.next
                curr_node.next = new_node
            curr_node = curr_node.next
            count += 1
        return

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
        return size

    # Print values in the linked list, time complexity: O(n)
    def print_list(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            print("In the list we have ...")
            curr_node = self.head
            llist_str = ''
            while curr_node:
                llist_str += str(curr_node.val) + '-->'
                curr_node = curr_node.next
            print(llist_str)

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

    # remove value at the given index in the linked list, time complexity: O(n)
    def remove_at(self,ind):
        if ind < 0 or ind > self.get_length():
            raise Exception("Out of Bound")

        if ind == 0:
            self.remove_at_begin()
            return

        if ind == self.get_length():
            self.remove_at_end()
            return

        else:
            count = 0
            curr_node = self.head
            while curr_node:
                if count == ind-1:
                    curr_node.next = curr_node.next.next
                count +=1
                curr_node = curr_node.next

    # insert value after a given value in the linked list, time complexity: O(n)
    def insert_after_value(self,val,new_val):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.val == val:
                    new_node = ListNode(new_val,curr_node.next)
                    curr_node.next = new_node
                curr_node = curr_node.next

    # remove value after a given value in the linked list, time complexity: O(n)
    def remove_by_value(self,val):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next:
                if curr_node.next.val == val:
                    curr_node.next = curr_node.next.next
                curr_node = curr_node.next

    # Reverse a linked list iteratively
    def reverse_list(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            prev_node = None
            while curr_node:
                temp_next = curr_node.next
                curr_node.next=prev_node
                prev_node = curr_node
                curr_node = temp_next
        self.head = prev_node

    def search(self,val):
        if self.head is None:
            return
        else:
            curr_node = self.head
            count = 0
            while curr_node:
                if curr_node.val == val:
                    print(str(val)+" is found at index "+ str(count))
                    return
                curr_node = curr_node.next
                count += 1



ll = LinkedList()
ll.insert_at_begin(10)
ll.insert_at_begin(20)
ll.insert_at_begin(30)
ll.insert_at_begin(40)
# ll.print_list()
# ll.insert_at_end(50)
# ll.print_list()
# ll.insert_multiple([11,12,13])
# ll.print_list()
# print("length:", str(ll.get_length()))
# ll.remove_at_begin()
# ll.print_list()
# ll.remove_at_end()
# ll.print_list()
ll.insert_at(0,15)
#ll.insert_at(12,13)
ll.insert_at(5,22)
ll.print_list()
ll.remove_at(3)
ll.print_list()
ll.insert_after_value(40,32)
ll.print_list()
ll.remove_by_value(30)
ll.print_list()
ll.reverse_list()
ll.print_list()
ll.search(40)