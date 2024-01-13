class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.insert(0,value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if len(self.q) > 0:
            self.q.popleft()
            return True
        return False
        

    def deleteLast(self) -> bool:
        if len(self.q) > 0:
            self.q.pop()
            return True
        return False        

    def getFront(self) -> int:
        if len(self.q) > 0:
            front = self.q[0]
            return front
        return -1
        

    def getRear(self) -> int:
        if len(self.q)> 0:
            rear =  self.q[-1]
            return rear
        return -1
        

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        

    def isFull(self) -> bool:
        if len(self.q) == self.k:
            return True
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()