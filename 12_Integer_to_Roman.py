class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        roman_eq = ""
        unit = 1
        while(num > 0):
            digit = num % 10
            if digit == 0:
                unit *= 10
                num = num // 10
                continue
            if digit < 5:
                if digit != 4:
                    roman_eq = (mappings[unit] * digit) + roman_eq
                else:
                    roman_eq = (mappings[unit] + mappings[(5 * unit)]) + roman_eq
            elif digit == 5:
                roman_eq = (mappings[unit * 5]) + roman_eq
            else:
                if digit != 9:
                    roman_eq = (mappings[(5 * unit)] + (mappings[unit] * (digit - 5))) + roman_eq
                else:
                    roman_eq = (mappings[unit] + mappings[(10 * unit)]) + roman_eq
            unit *= 10
            num = num // 10
        return roman_eq