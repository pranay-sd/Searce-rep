import heapq as hp

"""
Here heapq module uses minheap and so the structure
of the heap is according to min heap and popping an
elements returns the smallest one.
"""

#M1 : define a list and heapify it
li1 = [1,2,6,3,5,4,9]
hp.heapify(li1)
print(list(li1))

#M2 : define an empty list and push elements
li2 = []
hp.heappush(li2,1)
hp.heappush(li2,2)
hp.heappush(li2,6)
hp.heappush(li2,3)
hp.heappush(li2,5)
hp.heappush(li2,4)
hp.heappush(li2,9)
print(li2)

#Popping an element(smallest)
print(hp.heappop(li1))
print(li1)

#This method first pushes the element and 
#then pop the smallest element 
print(hp.heappushpop(li2,8))
print(li2)

#To get k-largest/smallest elements in the list
# in descending/ascending order
L = hp.nlargest(3,li1)
print(L)

print(hp.nsmallest(3,li2))

#This method first pop the smallest element 
# and then pushes the element mentioned
print(hp.heapreplace(li1,8))
print(li1)

#print(hp.merge(li1,li2))