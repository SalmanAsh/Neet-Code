class Anagram:
    def is_Anagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


test = Anagram()
print(test.is_Anagram(s='salman', t='namlas'))
print(test.is_Anagram(s='salman', t='defefe'))
print(test.is_Anagram(s='hello', t='olleh'))
print(test.is_Anagram(s='frfr', t='namlrgrgas'))
print(test.is_Anagram(s='salfddfman', t='namfdfelas'))
print(test.is_Anagram(s='cat', t='tac'))
print(test.is_Anagram(s='yeknom', t='monkey'))
