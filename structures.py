class Stack:
    def __init__(self):
        self.stack : list = []

    def __str__(self) -> str:
        return str(self.stack)

    def is_empty(self):
        return self.stack == []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peak(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)    