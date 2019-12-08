class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        
        while start < end:
            mid = (start + end) // 2
            if sum(-(-i // mid) for i in nums) > threshold:
                start = mid + 1
            else:
                end = mid
        return start