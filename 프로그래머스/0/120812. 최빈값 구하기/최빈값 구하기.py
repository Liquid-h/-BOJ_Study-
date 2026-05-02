from collections import Counter

def solution(array):
    answer = -1
    count = Counter(array)
    mode = count.most_common(2)
    if len(mode) > 1 and mode[0][1] == mode[1][1]:
        answer = -1
    else:
        answer = mode[0][0]
    return answer