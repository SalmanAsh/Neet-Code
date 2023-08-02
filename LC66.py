class Solution:
    def plusOne(self, digits):
        n = len(digits)
        digits = digits[::-1]
        
        for i in range(n):
            if(digits[i] < 9):
                digits[i] += 1
                return digits[::-1]
            digits[i] = 0
            
        new_number = [0] * (n + 1)
        new_number[0] = 1
        return new_number