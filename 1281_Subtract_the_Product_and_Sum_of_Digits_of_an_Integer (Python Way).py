from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        return reduce(operator.mul, digits) - sum(digits)