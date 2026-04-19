import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

result = [a[0]]
record = [(0, a[0])]

for i in range(1, n):
    if a[i] > result[-1]:
        result.append(a[i])
        record.append((len(result) - 1, a[i]))
    else:
        low_num = bisect.bisect_left(result, a[i])
        result[low_num] = a[i]
        record.append((low_num, a[i]))

lis_length = len(result)
print(lis_length)

ans = []
cur_idx = lis_length - 1

for i in range(n - 1, -1, -1):
    if record[i][0] == cur_idx:
        ans.append(record[i][1])
        cur_idx -= 1

ans.reverse()
print(*ans)