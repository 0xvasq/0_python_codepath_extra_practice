from queue import PriorityQueue
from signal import valid_signals



'''
class Block:
    def __init__(self, value, localTop):
        self.value = value
        self.localTop = localTop

class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1
            if self.top == 0:
                self.stack[self.top] = Block(value, value)
            else:
                if self.stack[self.top-1].localMax > value:
                    self.stack[self.top] = Block(value, self.stack[self.top - 1].localMax)
                else:
                    self.stack
                    self.stack[self.top] = Block(value, value)
        print(value, "added to the stack")

    def pop(self):
        if self.stack[self.top] == -1:
            print("stack is full")
        else:
            self.top -= 1

    def max(self):
        if self.stack[self.top] == -1:
            print("stakc is full")
        else: 
            print("max is: ", self.stack[self.top].localMax)
'''


























'''
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

'''

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


'''
MAX_CHARS = 26
MAX_WORD_SIZE = 30

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.frequency = 0
        self.indexMinHeap = -1
        self.child = [None] * MAX_CHARS

class MinHeapNode:
    def __init__(self,root,frequency,word):
        self.root = root
        self.frequency = frequency
        self.word = word  

class minHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.array = [None]* capacity

def newTrieNode():
    trieNode = TrieNode
    return trieNode

def createMinHeap(capacity):
    minHeap = minHeap(capacity)
    return minHeap

def buildMinHeap(minHeap):
    n = minHeap.count - 1
    for i in range((n - 1) // 2,-1,-1):
        minHeapify(minHeap, i)

def insertInMinHeap(minHeap, root, word):
    if root.indexMinHeap != -1:
        minHeap.array[root.indexMinHeap].frequency += 1
        minHeapify(minHeap, root.indexMinHeap)
    elif minHeap.count < minHeap.capacity:
        count = minHeap.count
        minHeap.array[count] = MinHeapNode(root,root.frequency,word)
        root.indexMinHeap = minHeap.count
        minHeap.count += 1
        buildMinHeap(minHeap) 
    elif root.frequency > minHeap.array[0].frequency:
        minHeap.array[0].root.indexMinHeap = -1
        minHeap.array[0].root = root
        minHeap.array[0].root.indexMinHeap = 0
        minHeap.array[0].frequency = root.frequency
        minHeap.array[0].word = word
        minHeapify(minHeap, 0)
    
       
def insertUtil(root, minHeap, word, dupWord):
    if root is None:
        root = newTrieNode
    if word:
        insertUtil(root.child[ord(word[0])-ord('a')], minHeap, word)
    else: 
        if root.isEnd:
            root.frequency += 1
        else:
            root.isEnd = True
            root.frequency = 1
        insertInMinHeap(minHeap, root, dupWord)
        
def displayMinHeap(minHeap):
    for i in range(minHeap.count):
        print(f"{minHeap.array[i].word}: {minHeap.array[i].frequency}")

def printKMostFreq(file_path, k):
    minHeap = createMinHeap(k)
    root = None

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                insertTriedAndHeap(word, root, minHeap)

'''

'''
class Solution(object):
    def mergeTwoList(self, list1, list2):
        dummyNode = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummyNode

'''

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

def addTwoNums(l1, l2):
    tempNode = ListNode()
    now = tempNode
    sum = 0
 

    while l1 or l2 or sum:
        if l1:
           num1 = l1.val
           l1 = l1.next
        else:
            num1 = 0

        if l2:
            num2 = l2.val
            l2 = l2.next
        else:
            num2 = 0

        sum_Total = num1 + num2 + sum
        sum = sum_Total // 10
        num = sum_Total % 10

        now.next = ListNode(num)
        now = now.next

        if sum > 0:
            now.next = ListNode(sum)

    return tempNode.next




if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    result = addTwoNums(l1, l2)

    while result:
        print(result.val, end=" ")
        result = result.next


'''

'''

class ListNode:
    def __init__(self, val=0,next=none):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = ListNode(0, head)
        left = temp
        curr = head

        while n > 0 and curr:
            curr = curr.next
            n-=1
        while curr:
            left = left.next
            curr = curr.next

        left.next = left.next.next
        return temp.next

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)

'''

def middleNode(head):
    if head is None:
        return None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

