class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.s:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.s[val]
            self.list[idx], self.s[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.s[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()