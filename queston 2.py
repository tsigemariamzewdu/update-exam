class Stack:
    def __init__(self,capacity):
        self.stack=[]
        self.capacity=capacity
        self.count=0
    def push(self,element):
        if self.IsFull():
            return "the stack is full"
        else:
            self.stack.append(element)
        self.count+=1
       
    
   
    def pop(self):
        if self.IsEmpty():
            return "the stack is empty"
         
        else:
            self.stack.pop()
    def peek():
        if self.IsEmpty():
            return "the stack is empty")
        else:
            return self.stack[-1]
    def IsEmpty(self):
        return self.size==0
        
    def size(self):
        return self.count
    def IsFull(self):
        return self.size==self.capacity

mystack=Stack(4)
mystack.push(6)
mystack.push(8)
mystack.push(4)
mystack.push(5)
print(mystack.stack)
mystack.pop()
print(mystack.IsFull())