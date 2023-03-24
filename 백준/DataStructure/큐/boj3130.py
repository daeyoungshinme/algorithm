# m으로 나누어 떨어지는 수 고로 m을 곱해서 n자리수를 만들어서 비교 처리

n, m = map(str, input().split())
i = 0
answer = 0

while len(number) < 6:
    i += 1
    number = m * i
    di = n/2
    if len(number) == n and number[:di] == str(number[di:n])[::-1] and number[n:n+di] == reversed(number[n+di:]):
        answer += 1
