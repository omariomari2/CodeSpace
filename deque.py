class Empty(Exception):
    pass 

class Deque:
    def __init__(self, default_size=10):
        self.default_size = default_size
        self.arr = [None] * self.default_size
        self.size = 0
        self.front = 0 

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.arr[self.front]

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.arr[(self.front + self.size - 1) % len(self.arr)]

    def resize(self):
        new_capacity = 2 * len(self.arr)
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.arr[(self.front + i) % len(self.arr)]
        self.arr = new_queue
        self.front = 0

    def add_first(self, e):
        if self.size == len(self.arr): 
            self.resize()
        self.front = (self.front - 1) % len(self.arr)  
        self.arr[self.front] = e
        self.size += 1

    def add_last(self, e):
        if self.size == len(self.arr):  
            self.resize()
        pos = (self.front + self.size) % len(self.arr)
        self.arr[pos] = e
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        item = self.arr[self.front]
        self.arr[self.front] = None  
        self.front = (self.front + 1) % len(self.arr)
        self.size -= 1
        return item

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        last_index = (self.front + self.size - 1) % len(self.arr)
        item = self.arr[last_index]
        self.arr[last_index] = None 
        self.size -= 1
        return item
