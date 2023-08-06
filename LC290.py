class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        function = {} # pattern: word
        seen = set()
        words = s.split(" ")
        if (len(words) != len(pattern)):
            return False
        for i in range(len(pattern)):
            if pattern[i] in function and words[i] != function.get(pattern[i]):
                return False
            elif pattern[i] in function and words[i] == function.get(pattern[i]):
                continue
            if(words[i] in seen): return False
            function[pattern[i]] = words[i]
            seen.add(words[i])
        
        return True