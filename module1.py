
from ctypes import sizeof
from optparse import Values
from socket import SO_VM_SOCKETS_BUFFER_MAX_SIZE
from typing import ValuesView
from xml.dom import ValidationErr


class Block:
    def __init__(self, value,localMax):
        self.value = value
        self.localMax = localMax

class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size 
        self.top = -1

    def push(self, value):

        if self.top == self.size - 1:
            print("Full stack")
        else:
            self.top += 1

            if self.top == 0:
                self.stack[self.top] = Block(value, value)
            else:
                if self.stack[self.top - 1].localMax > value:
                    self.stack[self.top] = Block(value, self.stack[self.top -1].localMax)

                else:
                    self.stack
                    self.stack[self.top] = Block(value, value)

            print(value, "inserted in the stack")

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else: 
            self.top -= 1
            print("Element popped")

    def max(self):
        if self.top == -1:
            print("stack is empty")
        else:
            print("Maximun value in the stack", self.stack[self.top].localMax)


stack = Stack(5)
stack.push(2)
stack.max()
stack.push(6)
stack.max()
stack.pop()
stack.max()



#1) understand  
#    -Ask clarifying questions and use examples to understand what the interviewer wants out of this problem
#    -Choose a “happy path” test input, different than the one provided, and a few edge case inputs. Verify that you and the interviewer are aligned on the expected inputs and outputs.
#2) Match
#    -See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
#3) Plan
#   -Sketch visualizations and write pseudocode
#   -Walk through a high level implementation with an existing diagram
#4) Implent
#    -Implement the solution (make sure to know what level of detail the interviewer wants)
#5) review 
#    -Re-check that your algorithm solves the problem by running through important examples
#    -Go through it as if you are debugging it, assuming there is a bug
#6) evaluate
#    -Finish by giving space and run-time complexity
#    -Discuss any pros and cons of the solution

