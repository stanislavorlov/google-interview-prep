import queue
from collections import deque

q = queue.Queue()
dq1 = deque([])
dq2 = deque([])
stack = []

for i in range(1,5):
    q.put(i)
    dq1.append(i)
    dq2.appendleft(i)
    stack.append(i)

print("Queue")
print(q.get())
print(q.get())

print("Dequeue Queue (appendLeft)")
print(dq2.pop())
print(dq2.pop())

print("Dequeue Stack (append)")
print(dq1.pop())
print(dq1.pop())

print("Stack")
print(stack.pop())
print(stack.pop())