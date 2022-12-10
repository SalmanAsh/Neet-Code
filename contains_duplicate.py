def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(containsDuplicate(nums=[1, 2, 3, 5, 1]))
print(containsDuplicate(nums=[1, 2, 3, 5, 6]))
print(containsDuplicate(nums=[1, 2, 3, 5, 2]))
print(containsDuplicate(nums=[1, 2, 3, 5, 50]))
print(containsDuplicate(nums=[1, 2, 3, 5, 9]))
print(containsDuplicate(nums=[1, 2, 3, 5, 5]))
