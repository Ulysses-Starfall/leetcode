# coding:utf-8


class Stack:
    def __init__(self):
        self.stack = []

    def __call__(self, *args, **kwargs):
        return self.stack

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s())
    s.pop()
    s.pop()
    print(s())
