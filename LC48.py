class Solution:
    def rotateImage(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # Save top left value
                topLeft = matrix[top][l + i]
                
                # Move Bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # Move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # Move top left to top right
                matrix[top + i][r] = topLeft
                
            l += 1
            r -= 1
                