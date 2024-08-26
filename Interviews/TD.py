# pylint: disable:invalid-name
def reverse_parentheses(s: str) -> str:
    """ Reverse only the string inside the parenthesis"""
    stack: list[str] = []
    
    for char in s:
        if char == ')':
            # Pop from stack until the matching '('
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()  # remove the '(' from the stack
            stack.extend(temp)  # push the reversed substring back to the stack
        else:
            stack.append(char)
    
    return ''.join(stack)

# Test cases
print(reverse_parentheses("foo(bar)baz")) # "foorabbaz"
print(reverse_parentheses("foo(bar(baz))blim")) # "foobazrabblim"
print(reverse_parentheses("(bar)")) # "rab"
