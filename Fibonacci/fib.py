cache = {}
def nth(n):
    if (n in cache):
        return cache[n]
    if (n <= 1):
        return n
    sum_ = nth(n-1) + nth(n-2)
    cache[n] = sum_
    return sum_


for i in range(1000):
    print(nth(i))
