#Implementing stacks in python using deque python collections

from collections import deque as deq

stack = deq()

#Insterting an element at the top
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

#Deleting the top element
a=stack.pop()

#Printing the popped element
print(a)
