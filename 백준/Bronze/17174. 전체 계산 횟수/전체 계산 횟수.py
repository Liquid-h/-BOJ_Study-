import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = 0

while True:
    result += n
    n //= m
    if n == 0:
        break

print(result)