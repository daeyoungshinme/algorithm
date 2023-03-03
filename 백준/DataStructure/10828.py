import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    commands = input().rstrip().split()
    # print(commands)

    if commands[0] == 'push':  # push X: 정수 X를 스택에 넣는 연산이다.
        stack.append(commands[1])
    elif commands[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        print(0 if stack else 1)
    elif commands[0] == 'top':
        print(stack[-1] if stack else -1)