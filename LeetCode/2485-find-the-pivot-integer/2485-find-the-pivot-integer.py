class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = sum(range(1, n + 1))
        result = 0
        for i in range(1, n + 1):
            result += i
            if result == total_sum:
                return i
            total_sum -= i
        return -1