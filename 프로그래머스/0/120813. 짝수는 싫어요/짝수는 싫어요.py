def solution(n):
    answer = []
    while True:
        if not answer:
            answer.append(1)
        else:
            answer.append(answer[-1] + 2)
        if answer[-1] > n:
            answer.pop()
            break
    return answer