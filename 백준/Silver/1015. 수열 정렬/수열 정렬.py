import sys
input = sys.stdin.readline

# 꿍실냐옹~!

n = int(input())
a = list(map(int, input().split()))

Good_Bye_Boj = []
for i in range(n):
    Good_Bye_Boj.append((a[i], i))

Good_Bye_Boj.sort()

p = [0] * n
for i in range(n):
    v, index = Good_Bye_Boj[i]
    p[index] = i

print(*(p))