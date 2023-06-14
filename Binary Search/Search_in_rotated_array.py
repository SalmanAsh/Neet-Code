#My solution
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while(l <= r):
            mid = (r + l) // 2
            
            if(nums[mid] == target):
                return mid
            if(nums[mid] > nums[l]):
                if(target < nums[l]or target > nums[mid]):
                    l = mid + 1
                else:
                    r = mid - 1
            elif(nums[mid] < nums[l]):
                if(target < nums[mid] or target > nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                
        

test = Solution()
print(test.search([4, 5, 6, 7, 0, 1, 2], 0))

print(test.search([4, 5, 6, 0, 1, 2, 3], 0))

#[4, 5, 6, 7, 8, 0, 1, 2]
#[4, 5, 6, 7, 0, 1, 2]
#[l         m        r]

#[4, 5, 6, 0, 1, 2, 3, 3.5]
#[l           m        r]



class Solution2:
    def bin(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while(l <= r):
            mid = (r + l) // 2
            
            if (nums[mid] == target):
                return mid
            #left portion
            if (nums[mid] >= nums[l]):
                if (target > nums[mid] or target < nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if (target < nums[mid] or target > nums[r]):
                     r = mid - 1
                elif(target > nums[mid] or target < nums[l]):
                    l = mid + 1
                
        
        return -1

test = Solution2()
print(test.bin([4, 5, 6, 7, 0, 1, 2], 0))

print(test.bin([4, 5, 6, 0, 1, 2, 3], 0))