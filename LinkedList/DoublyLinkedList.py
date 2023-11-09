class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = None(data)
    
    def tail_next_append(self, data):
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        current.next.pre = current
    
    def target_next_one_append(self, data, target):
        new_node = Node(data)
        if self.head.data == target:
            self.head.next.pre = new_node
            self.head.next = new_node
            return
        
        current = self.head
        while current.next:
            if current.next.data == target:
                current.next.next.pre = new_node
                current.next.next = new_node
                return
            
        print("Don't find the target to append the new node.")

    
    def tail_delete(self):
        current = self.head
        while current.next:
            current = current.next
        
        current.pre.next = None
    
    def one_search(self, target):
        if self.head.data == target:
            return target
        
        current = self.head
        while current.next:
            if current.next == target:
                return target
            current = current.next
        
        print("Don't find the target.")

    
    def all_search(self, target):
        if self.head.data == target:
            print(target)
        
        current = self.head
        while current.next:
            if current.next == target:
                print(target)
            current = current.next
        
        print("Over")

    def one_change(self, data, target):
        if self.head.data == target:
            print(self.head.data + "↓")
            self.head.data = data
            print(self.head.data)
            return
        
        current = self.head
        while current.next:
            if current.next.data == target:
                print(current.next.data + "↓")
                current.next.data = data
                print(current.next.data)
                return
            current = current.next
        
        print("Don't find the target.")
    