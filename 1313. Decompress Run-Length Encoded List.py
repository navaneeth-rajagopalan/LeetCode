class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        solution = []
        for i in range(0, len_nums, 2):
            solution += [nums[i + 1] for j in range(nums[i])]
        return solution
