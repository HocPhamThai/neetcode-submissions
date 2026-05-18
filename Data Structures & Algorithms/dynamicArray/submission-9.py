class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = max(1, capacity)
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.arr[i]
        else:
            return "Index out of bound"


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.arr[i] = n
        else:
            return "Index out of bound"

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if(self.size == 0):
            raise IndexError("Array is empty")
        element = self.arr[self.size - 1]
        self.size -= 1
        return element

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity