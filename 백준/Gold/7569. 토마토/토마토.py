from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    tomato.append(box)

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                queue.append((h, n, m))

# 위, 아래, 앞, 뒤, 왼, 오
dh = [0, 0, 0, 0, 1, -1]
dn = [1, -1, 0, 0, 0, 0]
dm = [0, 0, 1, -1, 0, 0]

while queue:
    h, n, m = queue.popleft()
    for d in range(6):
        nh = h + dh[d]
        nn = n + dn[d]
        nm = m + dm[d]
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if tomato[nh][nn][nm] == 0:
                tomato[nh][nn][nm] = tomato[h][n][m] + 1
                queue.append((nh, nn, nm))

answer = 0
for box in tomato:
    for row in box:
        for t in row:
            if t == 0:
                print(-1)
                exit(0)
            answer = max(answer, t)

print(answer - 1)