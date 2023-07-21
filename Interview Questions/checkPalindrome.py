def solution(inputString):
    # Even Length words
    l, r = (len(inputString) // 2) - 1, len(inputString) // 2
    while(l >= 0 and r < len(inputString)):
        if (inputString[l] != inputString[r]):
            break
        elif(l == 0 and r == len(inputString) - 1):
            return True
        
        l -= 1
        r += 1
    
    # Odd Length words
    l = len(inputString) // 2
    r = l
    while(l >= 0 and r < len(inputString)):
        if (inputString[l] != inputString[r]):
            return False
        l -= 1
        r += 1
    
    return True

def is_palindrome(s: str) -> bool:
    length = len(s)
    
    for i in range(length//2):
        if (s[i] != s[length - i - 1]):
            return False
    
    return True