class Solution:
    def par(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if (c in close_to_open):
                if (stack and stack[-1] == close_to_open[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if (len(stack) == 0):
            return True
        return False


test = Solution()
print(test.par("[{()}]"))
print(test.par("[{()]"))
