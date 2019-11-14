class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        nums_len = len(nums)
        for i in range(nums_len):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i