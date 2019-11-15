class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == val:
                if nums[fast] != val:
                    swapper = nums[fast]
                    nums[fast] = nums[slow]
                    nums[slow] = swapper
                    slow += 1
            else:
                slow += 1
        return slow
        