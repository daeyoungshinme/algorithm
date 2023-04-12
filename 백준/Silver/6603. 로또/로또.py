def dfs(depth, start):
    global n
    if depth == 6:
        print(*result)
        return
    
    for i in range(start, n):
        result.append(nums[i])
        dfs(depth +1, i + 1 )
        result.pop()

result = []
while True:
    n, *nums = map(int,input().split())
    
    if n == 0:
        break
    
    dfs(0,0)    
    print()