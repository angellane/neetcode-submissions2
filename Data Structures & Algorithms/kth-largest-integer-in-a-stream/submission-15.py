class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = nums
        heapq.heapify(self.heap)
        self.heap.sort()

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return self.heap[-self.k]
        
        
