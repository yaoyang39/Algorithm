class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        if not self.head:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Linked List:")
    linked_list.display()

    target = 2
    if linked_list.search(target):
        print(f"{target} found in the linked list.")
    else:
        print(f"{target} not found in the linked list.")

    target = 5
    if linked_list.search(target):
        print(f"{target} found in the linked list.")
    else:
        print(f"{target} not found in the linked list.")

    target = 3
    linked_list.delete(target)
    print(f"{target} deleted from the linked list:")
    linked_list.display()