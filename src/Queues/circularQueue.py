#queue node class, for items in the queue
class QueueNode:
    def __init__(self, val=-1):
        self.val = val
        self.prev = None
        
    def setPrev(self, prev):
        self.prev = prev
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        
        # make invalid nodes for first and last
        self.first = QueueNode()
        self.last = QueueNode()

    def enQueue(self, value: int) -> bool:
        # if size remaining, add node
        if self.size < self.capacity:
            
            node = QueueNode(value)
            # if the first node then update the first pointer
            if self.isEmpty():
                self.first = node
            
            # make the current last node have prev point to newly added node
            self.last.setPrev(node)            
            # update last pointer to the newly added node
            self.last = node

            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():

            # if there is a valid first node, then update the pointer
            if self.Front() != -1:
                self.first = self.first.prev
            # else make the first pointer null value
            else:
                self.first = QueueNode()

            # if the size is 1, then the last pointer also points to the first node, update last pointer as well
            # if self.first == self.last:
            if self.size == 1:
                self.last = QueueNode()

            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        # return first value
        if self.first:
            return self.first.val
        return -1

    def Rear(self) -> int:
        # return last value
        if self.last:
            return self.last.val
        return -1

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.capacity else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()