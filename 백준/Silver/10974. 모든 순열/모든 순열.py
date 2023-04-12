from itertools import permutations

n = int(input())
nums = [i for i in range(1,n+1)]

for a in list(permutations(nums, n)):
    print(*a)