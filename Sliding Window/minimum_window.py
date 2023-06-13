class Solution1:
    def window(self, s: str, t: str) -> str:
        need = {}
        have = {}
        for i in range(len(t)):
            print(i)
            need[t[i]] = 1 + need.get(i, 0)
        need_length = len(need)
            
        res = []
        l = 0
        for r in range(len(s)):
            if (s[r] in need):
                have[s[r]] = 1 + have.get(r, 0)
            have_length = len(have)
            while(have_length == need_length):
                if(res):
                    if((res[1] - res[0]) > (r - l)):
                        res[0] = l
                        res [1] = r
                else:
                    res.append(l)
                    res.append(r)
                if (s[r] in need):
                    have[s[r]] = have.get(r, 0) - 1
                l += 1
            r += 1
        if res:
            return s[l:r]
        return ""

# test = Solution1()
# print(test.window("ADOBECODEBANC", "ABC"))

class Solution2:
    def sub(self, s: str, t: str) -> str:
        if t == "":
            return ""
        res = [-1, -1]
        resLen = float("infinity")
        Tcount = {}
        window = {}
        
        for i in t:
            Tcount[i] = 1 + Tcount.get(i, 0)
        
        have = 0
        need = len(Tcount)
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            if char in Tcount and window[char] == Tcount[char]:
                have += 1
            
            while (have == need):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if (s[l] in Tcount and window[s[l]] < Tcount[s[l]]):
                    have -= 1
                l += 0
        
        return s[res[0] : res[1]+1] if resLen != float("infinity") else ""
                
test = Solution2()
print(test.sub("ADOBECODEBANC", "ABC"))