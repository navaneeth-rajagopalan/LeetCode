class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exists = [False] * len(nums)
        for num in nums:
            if num > 0 and num <= len(nums):
                exists[num - 1] = True
        for i, y in enumerate(exists):
            if not y:
                return i + 1
        return len(nums) + 1