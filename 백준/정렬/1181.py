import sys
input = sys.stdin.readline
n = int(input())

results = []

for _ in range(n):
    word = input().rstrip()
    results.append(word)

set_res = set(results)
resutls = list(set_res)
print(resutls)
results.sort()
print(results)
print('\n'.join(sorted(results,key=len)))