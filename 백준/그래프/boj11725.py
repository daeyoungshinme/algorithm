import sys
input = sys.stdin.readline

# 특정 원소가 속한 집한을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 노드의 개수
n = int(input())

# 부모 노드 저장하는 리스트
parent = [0] * (n + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

for i in range(2, n + 1):
    a,b = map(int, input().split())
    


    print(find_parent(parent,a))
    print(find_parent(parent,b))

    

