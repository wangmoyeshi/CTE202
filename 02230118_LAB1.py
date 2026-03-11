class CustomList:
    def __init__(self, capacity=10):
        self._array = [None] * capacity
        self._capacity = capacity
        self._size = 0
        print(f"Created new CustomList with capacity {capacity}")
        print("Current size 0")

    def append(self, element):
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = element
        self._size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def set(self, index, element):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        return self._size

    def _resize(self):
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

# Example usage matching lab output
lst = CustomList()
lst.append(5)
print(f"Element at index 0: {lst.get(0)}")
lst.set(0, 10)
print(f"Element at index 0: {lst.get(0)}")
print(f"Current size: {lst.size()}")
