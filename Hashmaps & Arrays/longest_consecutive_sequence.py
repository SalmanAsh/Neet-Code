class Sequence:
    def long(self, nums: list[int]) -> int:
        n = sorted(nums)
        consecs = []
        seq = 1
        l = 0
        r = 1
        while (r <= len(n)-1):
            if (n[r] == n[l]+1):
                seq += 1
            else:
                consecs.append(seq)
                seq = 1
            l += 1
            r += 1
        return max(consecs)


test = Sequence()
i = [100, 4, 200, 1, 3, 2, 200, 5, 6]
print(test.long(i))


class Solution:
    def sequence(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


test1 = Solution()
print(test1.sequence(i))
