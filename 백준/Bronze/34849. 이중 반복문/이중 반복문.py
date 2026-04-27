import sys
input = sys.stdin.readline

n = int(input())

if n <= 10000:
    print("Accepted")

else: 
    print("Time limit exceeded")