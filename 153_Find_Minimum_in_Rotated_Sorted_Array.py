class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while(start < end):
            if nums[start] <= nums[end]:
                return nums[start]
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]