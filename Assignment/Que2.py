class SLLNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SLLNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node
    
def printLL(head):
    if head is None:
        print("Empty Linked List.")
        return
        
    itr = head

    while itr:
        print(itr.data)
        itr = itr.next

if _name__ == '__main__':
    llist_count = int(input())
    llist = SLL()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
        
    printLL(llist.head)