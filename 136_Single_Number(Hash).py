class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = set()
        for i in nums:
            if i in tracker:
                tracker.remove(i)
            else:
                tracker.add(i)
        for item in tracker:
            return item