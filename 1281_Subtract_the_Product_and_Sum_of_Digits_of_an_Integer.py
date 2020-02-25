class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_val, prod_val = 0, 1
        while n:
            unit_digit = n % 10
            n //= 10
            sum_val += unit_digit
            prod_val *= unit_digit
        return prod_val - sum_val