# stack
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())
print(stack[len(stack) - 1])

stack2 = []
stack2.append(10)
stack2.append(20)
stack2.append(30)
print(stack2.pop())
print(stack2.pop())
print(stack2.pop())

# queue
q = []
# enqueue
q.append(1)
q.append(2)
q.append(3)
# dequeue
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

from collections import deque
from queue import Queue

print("deque - stack")
data = deque()
data.append(1)
data.append(2)
data.pop()
print(data)

print("deque - queue")
data2 = deque()
data2.append(1)
data2.append(2)
data2.append(3)
data2.popleft()
print(data2)

print("Queue")
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())
print(queue.get())
print(queue.get())