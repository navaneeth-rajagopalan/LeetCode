class Solution:
    def search_pos(self, array, start, end, target):
        if start > end:
            return start
        search_index = start + ((end - start) // 2)
        if array[search_index] == target:
            return search_index
        if target < array[search_index]:
            return self.search_pos(array, start, search_index - 1, target)
        else: # target > array[searh_index]
            return self.search_pos(array, search_index + 1, end, target)
        
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search_pos(nums, 0, len(nums) - 1, target)