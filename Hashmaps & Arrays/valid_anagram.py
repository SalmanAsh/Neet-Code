class Anagram:
    """Method - one"""

    def is_Anagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


class Anag:
    """Method - two"""

    def is_Anag(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


# Test method one
test = Anagram()
print(test.is_Anagram(s='salman', t='namlas'))
print(test.is_Anagram(s='salman', t='defefe'))
print(test.is_Anagram(s='hello', t='olleh'))
print(test.is_Anagram(s='frfr', t='namlrgrgas'))
print(test.is_Anagram(s='salfddfman', t='namfdfelas'))
print(test.is_Anagram(s='cat', t='tac'))
print(test.is_Anagram(s='yeknom', t='monkey'))

print("----------------------")

# Test method two
test = Anag()
print(test.is_Anag(s='salman', t='namlas'))
print(test.is_Anag(s='salman', t='defefe'))
print(test.is_Anag(s='hello', t='olleh'))
print(test.is_Anag(s='frfr', t='namlrgrgas'))
print(test.is_Anag(s='salfddfman', t='namfdfelas'))
print(test.is_Anag(s='cat', t='tac'))
print(test.is_Anag(s='yeknom', t='monkey'))
