import sys
input = sys.stdin.readline

x, y = map(int, input().split())
r1 = '1' * x
r2 = '1' * y

print(int(r1) + int(r2))

    