class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        
        self.stack1.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
    
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        
        return self.stack2.pop()
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
    
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        
        print( self.stack2.pop())

    def is_empty(self):
        return not self.stack1 and not self.stack2


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()
