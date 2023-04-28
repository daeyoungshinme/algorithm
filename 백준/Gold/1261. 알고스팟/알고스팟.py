from collections import deque

def dfs(x,y,res):
    global answer
    # 끝에 도달하면 종료
    if x == M - 1 and y == N - 1:
        answer = min(answer, res)
        return
    
    for dx, dy in dist:
        tx = x + dx
        ty = y + dy
        
        if 0 <= tx < M and 0 <= ty < N and not visited[tx][ty]:
            visited[tx][ty] = True
            res += int(graph[tx][ty])
            dfs(tx,ty,res)
            visited[tx][ty] = False
            res -= int(graph[tx][ty])
            
def bfs():
    global answer
    queue = deque()
    queue.append((0,0)) # x,y,벽 허문 총수
            
    while queue:
        x,y = queue.popleft()
        
        for dx, dy in dxy:
            tx = x + dx
            ty = y + dy

            if 0 <= tx < M and 0 <= ty < N and dist[tx][ty] == -1:
                if graph[tx][ty] == '0':
                    dist[tx][ty] = dist[x][y]
                    queue.appendleft((tx,ty))
                else:
                    dist[tx][ty] = dist[x][y] + 1
                    queue.append((tx,ty))

N,M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(M)]
dist = [[-1] * N for _ in range(M)]

dxy = [(-1,0), (0,1), (0,-1), (1,0)]
answer = 1e9
result = []

dist[0][0] = 0
bfs()
print(dist[M-1][N-1])