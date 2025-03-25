class Empty(Exception):
    pass 

class Queue:
    def __init__(self, default_size = 10):
        self.default_size = default_size
        self.arr = [None] * self.default_size
        self.size = 0
        self.front = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return  self.size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self.arr[self.front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        item = self.arr[self.front]
        self.arr[self.front] = None
        self.front += 1
        self.size -= 1
        
        return item
    
    def resize(self):
        new_capacity = 2 * len(self.arr)
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.arr[(self.front + i) % len(self.arr)]
        
        self.arr = new_queue
        self.front = 0
        
    def enqueue(self, e):
        if self.size == len(self.arr):
            self.resize()
            
        pos = (self.size + self.front) % len(self.arr)
        self.arr[pos] = e
        self.size += 1
        
        
        
q = Queue(3)
print(q.is_empty())
q.enqueue(5)
q.enqueue(6)
q.enqueue('a')
print(q.first())
print(q.dequeue())
print(q.first())
