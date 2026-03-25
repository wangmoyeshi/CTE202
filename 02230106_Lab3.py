# Task 3: Implement the Node and LinkedStack Class Structure
class Node:
    """Node class that contains Data and Next fields"""
    def __init__(self, data):
        self.data = data
        self.next = None
# Task 4:Implement Linked List-based Stack Operations
class LinkedStack:
    """LinkedStack class with top reference and size counter"""
    def __init__(self):
        self._top = None
        self._size = 0
        print("Created new LinkedStack")

    def is_empty(self):
        """Check if the stack contains no elements"""
        return self._top is None

    def size(self):
        """Return the current number of elements"""
        return self._size

    def push(self, element):
        """Add an element to the top of the stack"""
        new_node = Node(element)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        print(f"Pushed {element} to the stack")

    def pop(self):
        """Remove and return the element at the top"""
        if self.is_empty():
            return None
        popped_node = self._top
        self._top = self._top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        """Return the element at the top without removing it"""
        if self.is_empty():
            return None
        return self._top.data

    def display(self, mode="list"):
        """Show all elements in the stack"""
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next
        
        if mode == "list":
            # Format: Display stack:[30,20,10]
            print(f"Display stack:[{','.join(elements)}]")
        else:
            # Format: Current stack: 20 -> 10 -> null
            print(f"Current stack: {' -> '.join(elements)} -> null")

# Execution to match requirements ---
if __name__ == "__main__":
    # Initialize stack
    ls_stack = LinkedStack()
    
    # Required Output: Stack is empty: True
    print(f"Stack is empty: {ls_stack.is_empty()}")
    
    # Push 10
    ls_stack.push(10)
    ls_stack.display(mode="list")
    
    # Push 20
    ls_stack.push(20)
    ls_stack.display(mode="list")
    
    # Push 30
    ls_stack.push(30)
    ls_stack.display(mode="list")
    
    # Peek and Pop
    print(f"Top element: {ls_stack.peek()}")
    print(f"Popped element: {ls_stack.pop()}")
    
    # Final display and size
    ls_stack.display(mode="arrow")
    print(f"Stack size: {ls_stack.size()}")