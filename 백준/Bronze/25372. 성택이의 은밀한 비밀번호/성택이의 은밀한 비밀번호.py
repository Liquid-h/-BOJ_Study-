import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = input().rstrip()
    if len(n) >= 6 and len(n) <= 9:
        print("yes")

    else:
        print("no")