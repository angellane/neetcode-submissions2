class RandomizedSet:

    def __init__(self):
        self.obj = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.obj:
            self.obj.add(val)
            return False
        return True 
        

    def remove(self, val: int) -> bool:
        if val in self.obj:
            self.obj.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        rand = random.randrange(0, len(self.obj))
        listSet = list(self.obj)
        return listSet[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()