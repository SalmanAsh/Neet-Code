"""
2 solutions
"""

class Solution:
    """ Use binary search to find target"""
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """ My solution """
        
        for arr in matrix:
            if target >= arr[0] and target <= arr[-1]:
                return self.binary_search(arr, target)
        return False
    
    def binary_search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """ My solution """
        top = 0
        bottom = len(matrix) - 1
        
        while (top <= bottom):
            row = top + ((bottom - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                return self.binary_search(matrix[row], target)

        return False
    
    def binary_search(self, arr, target):
        """ O(log n)"""
        
        l = 0
        r = len(arr) - 1
        
        while(l <= r):
            m =  l + ((r - l) // 2)
            if(target < arr[m]):
                r = m - 1
            elif (target > arr[m]):
                l = m + 1
            else:
                return True
            
        return False