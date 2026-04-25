N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
Good_Bye_Boj = 0

for coin in reversed(coins):
    if K == 0:
        break
    Good_Bye_Boj += K // coin
    K = K % coin

print(Good_Bye_Boj)