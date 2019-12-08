class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        look_up = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        
        for char in s:
            if char in look_up:
                if len(stack) > 0 and stack.pop() == look_up[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False