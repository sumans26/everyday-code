# https://leetcode.com/problems/implement-queue-using-stacks/description/
from queue import LifoQueue

class MyQueue:
    

    def __init__(self):
        self.q1 = LifoQueue()
        self.q2 = LifoQueue()
        

    def push(self, x: int) -> None:
        self.q2.put(x)

    def pop(self) -> int:
        if(not self.q1.empty()):
            return self.q1.get()
        elif (not self.q2.empty()):
            while(not self.q2.empty()):
                self.q1.put(self.q2.get())
            return self.q1.get()
        else:
            return None

    def peek(self) -> int:
        if(not self.q1.empty()):
            obj =  self.q1.get()
            self.q1.put(obj)
            return obj
        elif (not self.q2.empty()):
            while(not self.q2.empty()):
                self.q1.put(self.q2.get())
            obj =  self.q1.get()
            self.q1.put(obj)
            return obj            
        else:
            return None

    def empty(self) -> bool:
        return(self.q1.empty() and self.q2.empty())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()