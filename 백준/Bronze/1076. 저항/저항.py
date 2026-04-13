import sys
input = sys.stdin.readline

color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
a = color.index(input().rstrip())
b = color.index(input().rstrip())
c = color.index(input().rstrip())

print((a*10+b)*pow(10,c))

