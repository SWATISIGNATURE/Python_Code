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


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self,val):
        return self.queue.insert_at_begin(val)

    def dequeue(self):
        return self.queue.remove_at_end()

    def peek(self):
        curr_node = self.queue.head
        while curr_node.next:
            curr_node = curr_node.next
        return print(curr_node.val)

    def rear(self):
        return print(self.queue.head.val)

    def isempty(self):
        return self.queue.head is None

    def size(self):
        return print(self.queue.get_length())

    def print(self):
        return self.queue.print_list()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.print()
    print(q.size())
    q.dequeue()
    q.print()
    print(q.peek())
    print(q.rear())
    q.isempty()