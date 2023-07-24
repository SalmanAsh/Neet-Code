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
}
