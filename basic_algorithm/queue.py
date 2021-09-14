# 큐: 먼저 들어온 데이터가 먼저 나감(선입선출)

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
