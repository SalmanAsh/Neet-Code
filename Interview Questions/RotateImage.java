public class RotateImage {
    public int[][] RotImg(int[][] matrix){
        int N = matrix.length;

        // Step 1 - Transpose The Matrix (Turn Rows to Cols)
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2 - Flip Horizontally
        for (int i = 0; i < N; i++){
            for (int j = 0; j < (N/2); j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][N - 1 - j];
                matrix[i][N - 1 - j] = temp;
            }
        }
        return matrix;
    }

    public int[][] solution(int[][] a) {
        int left = 0;
        int right = a.length - 1;
        
        while (left < right){
            for(int i = 0; i < right - left; i++){
                int top = left;
                int bottom = right;
                
                // Save top left value
                int topLeft = a[top][left + i];
                
                // Move bottom left to top left
                a[top][left + i] = a[bottom - i][left];
                
                // Move bottom right to bottom left
                a[bottom - i][left] = a[bottom][right - i];
                
                // Move top right to bottom right
                a[bottom][right - i] = a[top + i][right];
                
                // Move top left to top right
                a[top + i][right] = topLeft;
            }
            
            left++;
            right--;
        }
        return a;
    }
}
