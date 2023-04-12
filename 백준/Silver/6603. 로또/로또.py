from itertools import combinations

while True:
    n, *nums = map(int,input().split())
    
    if n == 0:
        break
    
    for a in list(combinations(nums, 6)):
        print(*a)
    
    print()