import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

result = []
idx = [0] * n

for i in range(n):
    if not result or a[i] > result[-1]:
        result.append(a[i])
        idx[i] = len(result) - 1
    else:
        p = bisect.bisect_left(result, a[i])
        result[p] = a[i]
        idx[i] = p

ans = []
l = len(result) - 1
for i in range(n - 1, -1, -1):
    if idx[i] == l:
        ans.append(a[i])
        l -= 1
        if l < 0:
            break

ans.reverse()
print(len(result))
print(' '.join(map(str, ans)))