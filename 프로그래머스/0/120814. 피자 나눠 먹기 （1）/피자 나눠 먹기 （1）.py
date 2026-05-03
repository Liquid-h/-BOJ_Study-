def solution(n):
    answer = 0
    while n > 0:
        answer += 1
        n -= 7
    return answer