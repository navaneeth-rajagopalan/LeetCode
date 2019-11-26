class Solution:            
        
    def search(self, nums: List[int], target: int) -> int:
        INF = float("inf")
        start, end = 0, len(nums) - 1
        while(start <= end):
            mid_point = start + ((end - start) // 2)
            if target == nums[mid_point]:
                return mid_point
            if (nums[mid_point] < nums[end]) == (target < nums[end]): # Mid and target in same halves
                comparator = nums[mid_point]
            else:
                if nums[mid_point] > target:
                    comparator = -INF
                else:
                    comparator = INF
            if target > comparator:
                start = mid_point + 1
            else:
                end = mid_point - 1
        return -1