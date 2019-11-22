class Solution:
    def calc_median(self, source, target, total_len, divider):
        if divider[0] == -1:
            left_max = target[divider[1]]
        else:
            left_max = max(source[divider[0]], target[divider[1]])
        if total_len % 2 == 0:
            #right_min = min(source[divider[0] + 1], target[divider[1] + 1])
            right_min = min(source[divider[0] + 1] if divider[0] + 1 < len(source) else target[divider[1] + 1], target[divider[1] + 1])
            return (left_max + right_min) / 2
        return left_max
    
    def recurse_median_search(self, source, target, total_len, mid_len, start, end):
        if start > end:
            return self.calc_median(source, target, total_len, [-1, mid_len - 1])
        source_index = start + ((end - start) // 2)
        target_index = mid_len - source_index - 1
        
        if source[source_index] > target[target_index]:
            return self.recurse_median_search(source, target, total_len, mid_len, start, source_index - 1)
        
        if (source_index + 1) >= len(source): # or (target_index - 1) <= 0:
            return self.calc_median(source, target, total_len, [source_index, target_index - 1])
        
        if source[source_index + 1] < target[target_index - 1]:
            return self.recurse_median_search(source, target, total_len, mid_len, source_index + 1, end)
        
        return self.calc_median(source, target, total_len, [source_index, target_index - 1])
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            target = nums2
            source = nums1
        else:
            target = nums1
            source = nums2

        source_len = len(source)
        target_len = len(target)
        
        total_len = source_len + target_len
        mid_len = (source_len + target_len + 1) // 2
        
        if source_len == 0:
            if total_len % 2 == 0:
                return (target[mid_len - 1] + target[mid_len]) / 2
            else:
                return target[mid_len - 1]
        
        if source[source_len - 1] <= target[0]: # Source --> Target
            print("Check")
            if mid_len > source_len: # Mid Point in target
                target_mid = mid_len - source_len
                if total_len % 2 == 0:
                    return (target[target_mid - 1] + target[target_mid]) / 2
                else:
                    return target[target_mid - 1]
            else:
                return (source[source_len - 1] + target[0]) / 2
            
        if target[target_len - 1] <= source[0]: # Target --> Source
            if total_len % 2 == 0:
                if source_len == target_len:
                    return (target[target_len - 1] + source[0]) / 2
                else:
                    return (target[mid_len - 1] + target[mid_len]) / 2
            else:
                return target[mid_len - 1]
        
        return self.recurse_median_search(source, target, total_len, mid_len, 0, source_len - 1)