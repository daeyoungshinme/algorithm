
def set_grapth():
    global M,N
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    

def dfs(n, depth):
    global result
    if depth == 5:
        result = 1
        return
    
    for i in graph[n]:
        if not visited[i] and not result:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False
    

N,M = map(int, input().split())
graph = [list() for _ in range(N)]
visited = [False] * N
result = 0
set_grapth()

for i in range(N):
    visited[i] == True
    dfs(i,0)
    visited[i] == False
      
print(result)