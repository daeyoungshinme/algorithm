m = int(input())

result = -1

for i in range(m // 5 ,-1,-1):
    changes = m - (5 * i)
    if changes % 2 == 0:    
        result = i + ( changes // 2)
        break     
    
print(result)