class Elements:
    """Method - one"""

    def frequency_of_k(self, nums: list[int], k: int):
        freq = {}
        for n in nums:
            freq[n] = 1+freq.get(n, 0)
        count = 0
        output = []
        for i in freq:
            # while count < 2:
            #     l = sorted(freq)
            #     output.append(l[i])
            #     count += 1
            print(i)


test = Elements()
test.frequency_of_k([3, 1, 1, 2, 2, 1, 1, 3, 3], 2)


class Solution:
    """Method - two"""

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


test = Solution()
print(test.topKFrequent([1, 1, 1, 2, 2, 3], 2))
