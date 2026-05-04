class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        x = [i for i in range(1, len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] in a:
                b.append(nums[i])
            elif nums[i] not in a:
                a.append(nums[i])
        for i in range(len(x)):
            if x[i] not in a:
                b.append(x[i])

        return b