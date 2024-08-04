class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif tokens[i] == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif tokens[i] == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif tokens[i] == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()