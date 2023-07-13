import java.util.HashSet;

public class LC36 {
    public boolean isValidSudoku(char[][] board){
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                char current_val = board[i][j];
                if (current_val != '.'){
                    if(!set.add(current_val + " found in row " + i) ||
                    !set.add(current_val + " found in column  " + j) ||
                    !set.add(current_val + " found in box " + i/3 + "-" + j/3)) return false; 
                }
            }
        }
        return true;
    }
}
