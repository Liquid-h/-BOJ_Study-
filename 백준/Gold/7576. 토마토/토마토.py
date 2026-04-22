from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1:
            queue.append((n, m))

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

while queue:
    n, m = queue.popleft()
    for d in range(4):
        nn = n + dn[d]
        nm = m + dm[d]
        if 0 <= nn < N and 0 <= nm < M:
            if tomato[nn][nm] == 0:
                tomato[nn][nm] = tomato[n][m] + 1
                queue.append((nn, nm))

answer = 0
for row in tomato:
    for t in row:
        if t == 0:
            print(-1)
            exit(0)
        answer = max(answer, t)

print(answer - 1)