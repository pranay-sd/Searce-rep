class Node:
    def __init__(self, data=None,next=None):

        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty Linked List.")
            return
        
        itr = self.head
        llstr = " "

        while itr:
            llstr += str(itr.data) + "->"
            itr = itr.next

        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count  == index-1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index < 0 or index >self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beg(data)

        count = 0
        itr = self.head
        while itr:
            if count  == index-1:
                node=Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count+=1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(6)
    ll.insert_at_beg(25)
    ll.insert_at_end(56)
    ll.insert_at_end(64)
    ll.print()
    ll.remove_at(1)
    ll.print()
    ll.insert_at(1,85)
    ll.print()
    print("length:",ll.get_length())