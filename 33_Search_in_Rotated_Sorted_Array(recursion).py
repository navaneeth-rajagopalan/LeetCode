class Solution:
    def search_pos(self, nums, start, end, target):
        if start > end:
            return -1
        mid_point = start + ((end - start) // 2)
        if nums[mid_point] == target:
            return mid_point
        if nums[mid_point] < nums[end]: # Pivot in left half
            if target > nums[mid_point]:
                if target <= nums[end]: # Search Right
                    return self.search_pos(nums, mid_point + 1, end, target)
                else: # Search Left
                    return self.search_pos(nums, start, mid_point - 1, target)
            else: # Search Left
                return self.search_pos(nums, start, mid_point - 1, target)
        else: # Pivot in right half
            if target > nums[mid_point]: # Search right
                return self.search_pos(nums, mid_point + 1, end, target)
            else:
                if target < nums[start]: # Search right
                    return self.search_pos(nums, mid_point + 1, end, target)
                else: # Search Left
                    return self.search_pos(nums, start, mid_point - 1, target)
            
        
    def search(self, nums: List[int], target: int) -> int:
        return self.search_pos(nums, 0, len(nums) - 1, target)