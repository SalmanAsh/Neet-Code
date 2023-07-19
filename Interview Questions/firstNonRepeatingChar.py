class Solution:
    def nonRepeatingChar(self, word: str) -> str:
        count = {}
        for s in word:
            count[s] = 1 + count.get(s, 0)
            
        for s in word:
            if count[s] == 1:
                return s
            
        return "_"