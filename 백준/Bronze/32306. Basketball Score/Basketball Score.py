import sys
input = sys.stdin.readline

team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

team1_result = 1 *team1[0] + 2 * team1[1] + 3 * team1[2]
team2_result = 1 *team2[0] + 2 * team2[1] + 3 * team2[2]

if team1_result > team2_result:
    print("1")
elif team1_result < team2_result:
    print("2")
else:
    print("0")