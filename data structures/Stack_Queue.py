from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def __str__(self):
        return ', '.join(self.container)

    """
    we can also use append left but with popleft 
    """
    def push(self, value):
        return self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def clear_stack(self):
        return self.container.clear()

    def reverse_string(self, s: str) -> str:
        return s[::-1]

    def balanced_paranthesis(self, s: str) -> bool:
        open = ['(', '[', '{']
        close = [')', ']', '}']
        relation = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = Stack()

        for c in s:
            if c in open:
                stack.push(c)
            elif c in close:
                if stack.isempty():
                    return False
                if relation[c] == stack.peek():
                    stack.pop()
                else:
                    return False
        return stack.isempty()
            

class Queue:
    def __init__(self):
        self.buffer = deque()

    def __str__(self):
        return '--> '.join(self.buffer)

    def enqueue(self, value):
        return self.buffer.append(value)   # we can also use insert() or appendleft() but to dequeue we're gonna need to use pop()

    def dequeue(self):
        return self.buffer.popleft()

    def clear_queue(self):
        return self.buffer.clear()


class CircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your CircularQueue object will be instantiated and called as such:
# obj = CircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

if __name__ == "__main__":
    s = Stack()
    s.push('Moroco')
    s.push('Tunisia')
    s.push('Libya')
    s.push('Algeria')
    print(s.reverse_string("We will conquere COVID-19"))
    print(s.balanced_paranthesis("))((a+b}{"))  # False
    print(s.balanced_paranthesis("[a+b]*(x+2y)*{gg+kk}"))
    print(s.balanced_paranthesis("[a+b]*(x+2y)*{gg+kk}{jx+rz)"))  # False
    print(s)


