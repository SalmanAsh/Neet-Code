class Solution:
    cache = {}
    def Nth(self, n):
        if(n <= 1):
            return n
        
        if(n in cache):
            return cache[n]
        
        add = self.Nth(n - 1) + self.Nth(n - 2)
        cache[n] = add
        return add

# test = Solution()
# print(test.Nth(500))

cache = {}
def Nth(n):
    if(n <= 1):
        return n
    
    if(n in cache):
        return cache[n]
    
    add = Nth(n - 1) + Nth(n - 2)
    cache[n] = add
    return add

print(Nth(20))