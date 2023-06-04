cache = {}
def nth(n):
    if (n in cache):
        return cache[n]
    if (n <= 1):
        return n
    sum = nth(n-1) + nth(n-2)
    cache[n] = sum
    return sum


for i in range(1000):
    print(nth(i))
