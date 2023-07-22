def solution(inputArray):
    res = inputArray[0] * inputArray[1]
    
    for l in range(len(inputArray)):
        res = max(res, inputArray[l] * inputArray[l + 1])
        
    return res