import sys
input = sys.stdin.readline # 반복문으로 여러줄 입력 받을때 쓸것!

n = int(input())
stack = []

for i in range(n):
    commands = input().rstrip().split()

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