class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_val = 1
        sum_val = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            prod_val *= digit
            sum_val += digit
        return prod_val - sum_val