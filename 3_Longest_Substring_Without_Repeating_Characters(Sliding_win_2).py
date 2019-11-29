class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, window_size, max_str = 0, 0, 0, 0
        seen = set()
        s_len = len(s)
        while(right < s_len):
            window_size += 1
            if s[right] in seen:
                max_str = max(max_str, window_size - 1)
                while(True):                    
                    seen.remove(s[left])
                    window_size -= 1
                    if s[left] == s[right]:
                        left += 1
                        break
                    left += 1
            seen.add(s[right])
            right += 1
        return(max(max_str, window_size))