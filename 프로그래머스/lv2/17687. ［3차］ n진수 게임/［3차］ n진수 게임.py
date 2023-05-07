def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]
    
    
def solution(n, t, m, p):
    answer = ''
    n_number = 0
    temp = '0'
    
    while len(answer) != t:
        if len(temp) >= int(m):
            answer += temp[int(p) - 1]
            temp = temp[int(m):] 
        else:
            n_number += 1
            temp += convert_notation(n_number, n)

    return answer




