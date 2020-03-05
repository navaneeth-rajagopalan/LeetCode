class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exists = 0
        for num in nums:
            if num > 0 and num <= len(nums):
                exists = exists | (1 << (num - 1))
        for i in range(len(nums)):
            if not (exists & (1 << i)):
                return i + 1
        return len(nums) + 1