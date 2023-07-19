import math
def solution(year):
    s = str(year)
    if (len(s) < 3): return 1
    
    if (len(s) == 3):
        century = s[0]
    elif(len(s) == 4):
        century = s[:2]
    
    if(int(s[-1]) > 0):
        return int(century) + 1
    return int(century)
    

print(solution(1905))


def solution(year):
    return math.ceil(year/100)
    