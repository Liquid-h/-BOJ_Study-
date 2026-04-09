import sys
input = sys.stdin.readline
# 이게 라이브러리 딸깍이 안되네;;

def find_seq(n,l):
    add = 0

    for i in range(l, 101):
            
        seq_sum = i*(i-1)//2
        diff = n - seq_sum
        if diff < 0:
            break

        if diff % i == 0 and diff // i >= 0:
            add = diff // i
            seq = [add + j for j in range(i)]
            return seq

    return [-1]

n, l = map(int, input().split())

seq = find_seq(n,l)

print(*seq)