N, M = map(int, input().split())
table = [input().strip() for _ in range(N)]

result = [0] * 26

for i in range(N):
    for j in range(M):
        c = table[i][j]
        count = 0
        for dx in [0, N]:
            for dy in [0, M]:
                x = i + dx
                y = j + dy
                Good_Bye_Boj = (x + 1) * (y + 1) * (2 * N - x) * (2 * M - y)
                count += Good_Bye_Boj
        result[ord(c) - ord('A')] += count

for Good_Bye_Boj in result:
    print(Good_Bye_Boj)