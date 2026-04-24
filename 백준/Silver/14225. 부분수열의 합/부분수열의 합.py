import sys
from itertools import combinations

# 꿍실냐옹~!

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

Good_Bye_Boj = set()

for i in range(1, n + 1):
    for combo in combinations(s, i):
        Good_Bye_Boj.add(sum(combo))

result = 1
while result in Good_Bye_Boj:
    result += 1

print(result)