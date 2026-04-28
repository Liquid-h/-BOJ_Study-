class Solution:
    def canMakeArithmeticProgression(self, arr):
        sorted_arr = sorted(arr)
        diff = sorted_arr[1] - sorted_arr[0]

        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] != diff:
                return False

        return True