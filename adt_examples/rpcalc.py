import numbers
from numbers import Number
import math

class RPcalc:
    def __init__(self):
        self.stack = []

    def push(self,n):
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "+":
            self.stack.append(self.stack.pop()+self.stack.pop())
        elif n == "-":
            self.stack.append(-(self.stack.pop()-self.stack.pop()))
        elif n == "*":
            self.stack.append(self.stack.pop()*self.stack.pop())
        elif n == "/":
            self.stack.append(1/(self.stack.pop()/self.stack.pop()))
        elif n == "sin":
            self.stack.append(math.sin(self.stack.pop()))
        elif n  == "cos":
            self.stack.append(math.cos(self.stack.pop()))


    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)