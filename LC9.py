class Solution:
    # My Solution
    def isPalindrome(self, x: int) -> bool:
        nums = str(x).strip()
        if(len(nums) % 2 == 0):
            l, r = (len(nums) // 2) - 1, (len(nums) // 2)
            while(l >= 0 and r < len(nums)):
                if(nums[l] == nums[r]):
                    l -= 1
                    r += 1
                else:
                    return False
            return True
        else:
            l, r = len(nums) // 2, len(nums) // 2
            while(l >= 0 and r < len(nums)):
                if nums[l] == nums[r]:
                    l -= 1
                    r += 1
                else:
                    return False
            return True
            
            