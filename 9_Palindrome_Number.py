class Solution:
        
    def isPalindrome(self, num: int) -> bool:
        if num >= 0 and (num % 10 != 0 or num == 0):
            rev_num = 0
            while(num > rev_num):
                rev_num = (rev_num * 10) + (num % 10)
                num = num // 10
            if(rev_num == num or num == (rev_num // 10)):
                return True
        return False