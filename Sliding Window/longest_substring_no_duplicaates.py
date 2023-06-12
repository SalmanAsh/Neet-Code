class Solution:
    def substring(self, s: str) -> int:
        counts = []
        l = 0
        r = 1
        while (l < len(s)-1):
            if (r == len(s)-1 and s[l] != s[r]):
                count = r - l
                counts.append(count)
                l += 1
                r = l+1
            elif (s[l] == s[r]):
                count = r - l
                counts.append(count)
                l += 1
                r = l+1
            else:
                r += 1
        return max(counts)


test = Solution()
print(test.substring("abcdabcdebb"))


class Solution2:
    def sub(self, s: str) -> int:
        charSet = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            count = max(count, r - l + 1)
        return count


test = Solution2()
print(test.sub("abcdabcdebb"))


class Solution3:
    def srf(self, s: str) -> int:
        counts = []
        l = 0
        r = 1
        while (l < len(s)-1):
            if(s[l]!=s[r] and r == len(s) -1):
                count = r - l + 1
                counts.append(count)
                l += 1
                r = l + 1
            elif(s[l]!=s[r]):
                r += 1
            elif(s[l]==s[r]):
                count = r - l + 1
                counts.append(count)
                l += 1
                r = l + 1
        return max(counts)

test = Solution3()
print(test.srf("abcde"))