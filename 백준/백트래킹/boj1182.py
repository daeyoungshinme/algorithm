
"""

"""
n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0  # 부분수열중 합이 0이되는것 카운트 변수
result = []


def dfs_c(k):
    global count
    if sum(result) == s and len(result) > 0:
        count += 1

    for i in range(k, len(num_list)):
        result.append(num_list[i])
        dfs_c(i+1)
        result.pop()


dfs_c(0)
print(count)
