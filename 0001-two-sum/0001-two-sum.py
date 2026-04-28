class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i+1:]:
                result.append(i)
                result.append(nums[i+1:].index(complement) + (i + 1))
                break
        return result