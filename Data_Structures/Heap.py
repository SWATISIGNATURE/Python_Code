"""
Heap
------------------
Heap data structure is mainly used to represent a priority queue
Properties:
    smallest of heap element is popped(min heap)
    Whenever elements are pushed or popped, heap structure in maintained.
    The heap[0] element also returns the smallest element each time.
    The value of the parent node in each level is less than or equal to its children’s values – min-heap.
    The value of the parent node in each level higher than or equal to its children’s values – max-heap.
    The min-heaps play a vital role in scheduling jobs, scheduling emails or in assigning the resources to tasks based on the priority.
        The parent node in index ‘i’ is less than or equal to its children.
        The left child of a node in index ‘i’ is in index ‘(2*i) + 1’.
        The right child of a node in index ‘i’ is in index ‘(2*i) + 2’.
    Max_heap: https://youtu.be/GnKHVXv_rlQ
Priority queues:
     the first element in the priority queue will be the one with the highest priority
     is_empty,insert,pop
     The programmer can decide whether the largest number is considered as the highest priority or the lowest number will be considered as the highest priority.
     If two elements have the same priority, then they appear in the order in which they appear in the queue i.e. its stable.
    priority queue is implemented in Python as a list of tuples where the tuple contains the priority as the first element and the value as the next element.

"""
# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created  min-heap : ",list(li))

heapq._heapify_max(li)
print("The created max heap is : ",list(li))
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))


heapq._heapify_max(li)
print(li)

# Priority Queue:
##############################
# import modules
import heapq as hq

# list of students
list_stu = [(5, 'Rina'), (1, 'Anish'), (3, 'Moana'), (2, 'cathy'), (4, 'Lucy')]

# Arrange based on the roll number
hq.heapify(list_stu)

print("The order of presentation is :")

for i in list_stu:
    print(i[0], ':', i[1])


pop_max = heapq._heappop_max(li)
print(pop_max)