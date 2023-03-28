# My Solution
class Solution:
    def pal(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while (left <= right):
            if (s[left].isalpha() and s[right].isalpha()):
                if (s[left].lower() != s[right].lower()):
                    return False
                else:
                    left += 1
                    right -= 1
            if (not s[left].isalpha()):
                left += 1
            if (not s[right].isalpha()):
                right -= 1
        return True


test = Solution()
print(test.pal("AB B A"))


class Solution2:
    def palindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalpha():
                newStr += c.lower()
        # Reversing a String
        if (newStr == newStr[::-1]):
            return True
        return False


test2 = Solution2()
print(test2.palindrome("ABC  CBA"))


# class Solution3:
#     def palin(self, s: str) -> bool:
#         l = 0
#         r = len(s)-1
#         while (l < r):
#             while (l < r and not self.alpha(s[l])):
#                 l += 1
#             while (r > l and not self.alpha(s[r])):
#                 r += 1
#             if (s[l].lower() != s[r].lower()):
#                 return False
#             l += 1
#             r += 1

#         def alpha(self, c):
#             if (ord("A") <= ord(c) <= ord('Z') or ord("a") <= ord(c) <= ord('z') or ord("0") <= ord(c) <= ord('9')):
#                 return True
#             return False


# test3 = Solution3()
# print(test3.palin("ABC  CBA"))
