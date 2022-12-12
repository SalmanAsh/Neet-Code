class Anagram:
    """Method - one"""

    def is_anagram(self, strs: list[str]):
        result = []
        for i in strs:
            for j in strs:
                anagrams = []
                if i != j and sorted(i) == sorted(j):
                    anagrams.append(i)
                    anagrams.append(j)
                    result.append(anagrams)
                else:
                    if i not in result:
                        result.append(i)
        return result


test = Anagram()
print(test.is_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))


class Solution:
    """Method - two"""

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # mapping charCount: listOfAnagrams
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26  # one for each character

            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()


test = Solution()
print(test.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
