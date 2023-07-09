class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        res = []
        sign = "+"
        for i in s:
            if i in nums:
                res.append(i)
            if i == "+":
                sign = "+"
            elif i == "-":
                sign = "-"
        
        res = int("".join(res))
        return res if sign == "+" else -res