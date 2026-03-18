# Task 1: Implement the Node and List Class Structure 
class Node:
    def __init__(self, data):
        self.data = data  # Data field to store element 
        self.next = None  # Next field to reference next node 

class LinkedList:
    def __init__(self):
        self.head = None      # Head reference to first node
        self.tail = None      # Tail reference (optional but recommended) 
        self.size_counter = 0 # Size counter to track elements 
        print("Created new LinkedList")

# Task 2: Implement Basic Operations 
    
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size_counter += 1
        print(f"Appended {element} to the list") 

    def get(self, index):
        if index < 0 or index >= self.size_counter:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.size_counter:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}") 
    def size(self):
        return self.size_counter

    def prepend(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size_counter += 1
        print(f"Prepend {element} to the list")

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Print Linked list : [{' '.join(elements)}]")


if __name__ == "__main__":
    ll = LinkedList()
    print(f"Current size: {ll.size()}") 
    print(f"Head: {ll.head}")

    ll.append(5)
    print(f"Element at index 0: {ll.get(0)}")
    
    ll.set(0, 10)
    print(f"Element at index 0: {ll.get(0)}") 
    print(f"Current size: {ll.size()}") 
    
    ll.prepend(10)
    ll.append(5) 
    ll.display()