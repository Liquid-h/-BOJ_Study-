def solution(array):
    array.sort()
    median = array[len(array) // 2]
    return median