class ArrayQueue:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._capacity = capacity
        print(f"Created new Queue with capacity: {self._capacity}")

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        if self._size == self._capacity:
            print("Queue is full")
            return
        # Calculate rear index using modulo for circular logic if needed, 
        # but here following standard linear addition for simplicity
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = element
        self._size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return answer

    def peek(self):
        if self.is_empty():
            return None
        return self._data[self._front]

    def size(self):
        return self._size

    def display(self):
        # Gather elements from front to rear
        elements = []
        for i in range(self._size):
            idx = (self._front + i) % self._capacity
            elements.append(self._data[idx])
        print(f"Display queue: {elements}")

# Testing for Part 1
if __name__ == "__main__":
    q = ArrayQueue(10)
    print(f"Queue is empty: {q.is_empty()}")
    q.enqueue(10)
    q.display()
    q.enqueue(20)
    q.display()
    q.enqueue(30)
    q.display()
    print(f"Front element: {q.peek()}")
    print(f"Dequeued element: {q.dequeue()}")
    q.display()
    print(f"Queue size: {q.size()}")

# --- PART 2: QUEUE IMPLEMENTATION USING LINKED LIST ---

# TASK 3: Implement the Node Class Structure
class Node:
    """Node class that contains data and next fields"""
    def __init__(self, data):
        self.data = data      # Data field to store the element 
        self.next = None      # Next field to reference the next node 

# TASK 3: Implement the LinkedQueue Class Structure
class LinkedQueue:
    """LinkedQueue class with front, rear, and size tracking """
    def __init__(self):
        self._front = None    # Front reference to the first node
        self._rear = None     # Rear reference to the last node
        self._size = 0        # Size counter to track the number of elements
        print("Created new Linked Queue") 

    # TASK 4: Implement is_empty Operation
    def is_empty(self):
        """Check if the queue contains no elements"""
        return self._size == 0

    # TASK 4: Implement enqueue Operation
    def enqueue(self, element):
        """Add an element to the rear of the queue"""
        newest = Node(element)
        if self.is_empty():
            self._front = newest
        else:
            self._rear.next = newest
        self._rear = newest
        self._size += 1
        print(f"Enqueued {element} to the queue") 

    # TASK 4: Implement dequeue Operation
    def dequeue(self):
        """Remove and return the element at the front"""
        if self.is_empty():
            return "Queue is empty"
        answer = self._front.data
        self._front = self._front.next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return answer

    # TASK 4: Implement peek Operation
    def peek(self):
        """Return the element at the front without removing it"""
        if self.is_empty():
            return None
        return self._front.data

    # TASK 4: Implement size Operation
    def size(self):
        """Return the current number of elements"""
        return self._size

    # TASK 4: Implement display Operation
    def display(self, style="list"):
        """Show all elements in the queue"""
        elements = []
        curr = self._front
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        
        if style == "list":
            # Matches early output: Display queue: [10, 20, 30] 
            print(f"Display queue: [{','.join(elements)}]")
        else:
            # Matches final output: Current queue: 20->30->null 
            print(f"Current queue: {'->'.join(elements)}->null")

# --- EXECUTION TO MATCH EXPECTED OUTPUT ---
if __name__ == "__main__":
    # Task 3 Initialization Output
    lq = LinkedQueue()
    print(f"Queue is empty: {lq.is_empty()}") # 
    
    # Task 4 Operations and Output
    lq.enqueue(10)
    lq.display(style="list") 
    
    lq.enqueue(20)
    lq.display(style="list") 
    
    lq.enqueue(30)
    lq.display(style="list") 
    
    print(f"Front element: {lq.peek()}")       
    print(f"Dequeued element: {lq.dequeue()}") 
    
    # Final display using the arrow format specified in Task 4 
    lq.display(style="arrow")                  
    print(f"Queue size: {lq.size()}")         