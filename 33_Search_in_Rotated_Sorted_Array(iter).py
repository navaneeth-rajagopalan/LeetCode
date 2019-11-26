class Solution:            
        
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while(start <= end):
            mid_point = start + ((end - start) // 2)
            if target == nums[mid_point]:
                return mid_point
            if nums[mid_point] < nums[end]: # Pivot in left half
                if target > nums[mid_point]:
                    if target <= nums[end]: # Search Right
                        start = mid_point + 1
                    else: # Search Left
                        end = mid_point - 1
                else: # Search Left
                    end = mid_point - 1
            else: # Pivot in right half
                if target > nums[mid_point]: # Search right
                    start = mid_point + 1
                else:
                    if target < nums[start]: # Search right
                        start = mid_point + 1
                    else: # Seatch left
                        end = mid_point - 1
        return -1