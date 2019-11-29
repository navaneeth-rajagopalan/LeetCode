class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_str = 0, 0
        seen = {}
        for right, val in enumerate(s):            
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            window_size = right - left + 1
            if window_size > max_str:
                max_str = window_size
            seen[val] = right
        return(max_str)