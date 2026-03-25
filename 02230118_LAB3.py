class ArrayStack:
    # --- Task 1: Class Structure 
    def __init__(self, capacity=10):
        """Initializes private array and top tracker """
        self.__array = [None] * capacity  # Private array
        self.__top = -1                   # Top tracker
        self.__capacity = capacity
        # Expected Output for Task 1 
        print(f"Created new ArrayStack with capacity: {self.__capacity}")

    # --- Task 2: Stack Operations
    def is_empty(self):
        """Checks if stack is empty [cite: 47]"""
        return self.__top == -1

    def size(self):
        """Returns number of elements [cite: 48]"""
        return self.__top + 1

    def push(self, element):
        """Adds element to top [cite: 44]"""
        if self.size() < self.__capacity:
            self.__top += 1
            self.__array[self.__top] = element
            # Expected Output for Task 2
            print(f"Pushed {element} to the stack")
        else:
            print("Stack Overflow")

    def pop(self):
        """Removes and returns top element [cite: 45]"""
        if self.is_empty():
            print("Stack Underflow")
            return None
        element = self.__array[self.__top]
        self.__array[self.__top] = None 
        self.__top -= 1
        return element

    def peek(self):
        """Returns top element without removing [cite: 46]"""
        if self.is_empty():
            return None
        return self.__array[self.__top]

    def display(self):
        """Shows all elements in stack [cite: 50]"""
        # Slicing to show current elements as a list 
        current_elements = [self.__array[i] for i in range(self.__top + 1)]
        print(f"Display stack: {current_elements}")

# --- Execution to match Expected Outcome 
if __name__ == "__main__":
    # Task 1 Expected Outcome 
    stack = ArrayStack(10)
    print(f"Stack is empty: {stack.is_empty()}")

    # Task 2 Expected Outcome
    stack.push(10)
    stack.display()
    
    stack.push(20)
    stack.display()
    
    stack.push(30)
    stack.display()
    
    print(f"Top element: {stack.peek()}")      
    print(f"Popped element: {stack.pop()}")   
    print(f"Stack size: {stack.size()}")      
    stack.display()                          