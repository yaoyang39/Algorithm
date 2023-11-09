class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class  CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        
        current = self.head
        if current.next !== self.head:
            current = current.next
        
        current.next = new_node
        current.next.next = self.head
    
    def append_specific(self, data, target):
        new_node = Node(data)
        