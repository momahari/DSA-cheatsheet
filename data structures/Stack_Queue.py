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


