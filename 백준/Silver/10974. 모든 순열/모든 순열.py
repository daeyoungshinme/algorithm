n = int(input())
nums = [i for i in range(1,n+1)]

visited = [False] * n

result = []

def dfs(depth):
    global n
    if depth == n:
        print(*result)
        return
    
    for i in range(len(nums)):
        if not visited[i]:
            result.append(nums[i])
            visited[i] = True
            dfs(depth + 1)
            result.pop()
            visited[i] = False
            
dfs(0)