class LRUCache:
    #we could use a queue to represent the order of a cache, when any operation is performed using that cache it is popped from the queue and reinserted at the right since that would mean it was used most recently
    #right -> most recent 
    #least recent <- left

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.usedOrder = deque()
        self.cache = {}

        

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.usedOrder.remove([key, value])
            self.usedOrder.append([key, value])
            return value
        else:
            return -1 
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldValue = self.cache[key]
            self.usedOrder.remove([key, oldValue])
        self.cache[key] = value
        self.usedOrder.append([key, value])
        
        while len(self.cache) > self.capacity:
            oldest = self.usedOrder.popleft()
            self.cache.pop(oldest[0])

        

        
        

