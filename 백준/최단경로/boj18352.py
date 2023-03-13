
import sys, heapq
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 도시 n, 도로 m, 거리 k, 출발 도시 x
n,m,k,x = map(int, input().split())

# 각 노드별 연결되어 있는 노드를 담고 있는 리스트 
graph = [[] for _ in range(n + 1)]

# 방문여부 체크
visited = [False] * (n + 1)

# 출발을 기점으로 최단거리 저장할 1차원 배열 각 인덱스를 해당 도시에 번호로 인식해야되서 n + 1 
distance = [INF] * (n + 1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
dijkstra(x)

isResult = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        isResult = True

if not isResult:
    print(-1)