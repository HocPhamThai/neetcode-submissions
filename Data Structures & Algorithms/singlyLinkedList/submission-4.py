class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count +=1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node 

    def remove(self, index: int) -> bool:
        if not self.head :
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        current = self.head
        prev = None
        count = 0
        while current and count != index:
            prev = current 
            current = current.next
            count += 1
        if not current:
            return False
        prev.next = current.next
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values
        
