import sys
from collections import deque
input = sys.stdin.readline 

n = int(input())
queue = deque([])

for _ in range(n):
    commands = input().split()

    if commands[0] == 'push':
        queue.append(commands[1])
    elif commands[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        print(0 if queue else 1)
    elif commands[0] == 'front':
        print(list(queue)[0] if queue else -1)
    elif commands[0] == 'back':
        print(list(queue)[-1] if queue else -1)
