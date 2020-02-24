class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [item for freq, val in zip(nums[0::2], nums[1::2]) for item in [val] * freq]