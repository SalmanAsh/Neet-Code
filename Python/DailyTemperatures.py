class DailyTemperatures:
    def solution1(self, temperatures: List[int]) -> List[int]:
        """ O(n^2) solution"""
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        
        return res

    def solution2(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            
            stack.append([t, i])
        
        return res