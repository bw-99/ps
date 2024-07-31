from collections import deque

def last_card():
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

n = int(input())
queue = deque(range(1, n + 1))
print(last_card())
