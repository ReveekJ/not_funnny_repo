class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        q = {')': '(',
             '}': '{',
             ']': '['}
        for i in s:
            if i in ['(', '{', '[']:
                stack.push(i)
            elif stack.top() == q[i]:
                stack.pop()
            else:
                return False
        if stack.top() is None:
            return True
        else:
            return False
