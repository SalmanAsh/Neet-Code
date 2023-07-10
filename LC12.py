class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        romans = [
            [1, 'I'],
            [4, 'IV'],
            [5, 'V'],
            [9, 'IX'],
            [10, 'X'],
            [40, 'XL'],
            [50, 'L'],
            [90, 'XC'],
            [100, 'C'],
            [400, 'CD'],
            [500, 'D'],
            [900, 'CM'],
            [1000, 'M']
        ]
        
        for i, sym in reversed(romans):
            count = num // i
            if count > 0:
                res += (sym) * count
                num -= i * count
            if num == 0:
                break
        
        return res
            