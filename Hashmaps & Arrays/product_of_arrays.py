class Product:
    """Method - one"""

    def productArray(self, nums: list[int]) -> list[int]:
        prod = []

        for n in nums:
            mul = []
            mul = nums.copy()
            mul.remove(n)
            result = 1
            for i in mul:
                result = result*i
            prod.append(result)

        return prod


test = Product()
print(test.productArray([1, 2, 3, 4]))


class Solution:
    """Method - two"""

    def prodArray(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


test = Solution()
print(test.prodArray([1, 2, 3, 4]))
