from collections import deque
import sys
input = sys.stdin.readline

Good_Bye_BOJ = int(input())
num = list(map(int, input().split()))
balloon = deque(range(Good_Bye_BOJ))
result = []


while balloon:
    idx = balloon.popleft()
    result.append(idx + 1)
    if not balloon:
        break
    n = num[idx]
   
    if n > 0:
        balloon.rotate(-(n - 1))
    else:
        balloon.rotate(-n)

print(' '.join(map(str, result)))