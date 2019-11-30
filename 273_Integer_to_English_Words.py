class Solution:
    def numberToWords(self, num: int) -> str:
        mappings = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }
        value = 1
        words = []
        if num == 0:
            return 'Zero'
        while (num > 0):
            triplet = num % 1000
            hundred = triplet // 100
            ten = (triplet // 10) % 10
            unit = triplet % 10
            sub_word = []
            if hundred > 0:
                sub_word.append(mappings[hundred])
                sub_word.append(mappings[100])
            if ten == 1:
                sub_word.append(mappings[triplet % 100])
            else:
                if ten > 1:
                    sub_word.append(mappings[ten * 10])
                if unit > 0:
                    sub_word.append(mappings[unit])
            if value > 1 and len(sub_word) > 0:
                sub_word.append(mappings[value])
            words = sub_word + words
            value *= 1000
            num = num // 1000
        return ' '.join(words)