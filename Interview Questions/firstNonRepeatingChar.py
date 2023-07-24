class Solution:
    def nonRepeatingChar(self, word: str) -> str:
        count = {}
        for s in word:
            count[s] = 1 + count.get(s, 0)
            
        for s in word:
            if count[s] == 1:
                return s
            
        return "_"

def solution(s):
    seen = set()
    duplicates = []
    
    for i in s:
        if i in seen and i not in duplicates:
            duplicates.append(i)
        else:
            seen.add(i)
    
    for i in s:
        if i not in duplicates:
            return i
    
    return "_"