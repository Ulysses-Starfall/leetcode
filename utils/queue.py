# coding:utf-8
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __call__(self, *args, **kwargs):
        return list(self.queue)

    def enqueue(self, ele):
        self.queue.append(ele)

    def dequeue(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q())
