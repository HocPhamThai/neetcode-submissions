class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = max(1, capacity)
        self.array = [1] * capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.array[i]
        else:
            return "Index out of bound"

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            return "Index out of bound"

    def pushback(self, n: int) -> None:
        if(self.size == self.capacity):
            self.resize() 
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if(self.size == 0):
            raise IndexError("Array is empty")
        element = self.array[self.size - 1]
        self.size -= 1
        return element

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity 
        self.array = new_array


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity