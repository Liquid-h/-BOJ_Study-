def solution(numbers):
    result = 0
    numbers.sort()
    if len(numbers) % 2 == 1:
        result = numbers[len(numbers) // 2]
        return result
    else:
        result = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
        return result