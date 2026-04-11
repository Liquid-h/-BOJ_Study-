import sys
input = sys.stdin.readline

level = int(input())

if level >= 200 and level <= 205:
    print(1)
elif level >= 206 and level <= 217:
    print(2)
elif level >= 218 and level <= 228:
    print(3)
else:
    print(4) # 정상화