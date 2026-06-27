class Solution:

    def __init__(self):
        self.symbolToValue = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }

    def intToRoman(self, num: int) -> str:
        output = ''
        # 4=IV, 9=IX, 40=XL, 90=XC, 400=CD, 900=CM

        if num in self.symbolToValue:
            output = self.symbolToValue[num]
        else:
            discharge = 1
            while num:
                digit = num % 10 * discharge
                if digit in self.symbolToValue:
                    output = self.symbolToValue[digit] + output
                elif digit + 1*discharge in self.symbolToValue:
                    output = self.symbolToValue[discharge] + self.symbolToValue[digit + 1*discharge] + output
                else:
                    while not digit in self.symbolToValue:
                        output = self.symbolToValue[discharge] + output
                        digit -= discharge
                    output = self.symbolToValue[digit] + output
                num //= 10
                discharge *= 10

        return output

solution = Solution()
# print(solution.intToRoman(3749))    # "MMMDCCXLIX"

print(solution.intToRoman(10))  # X