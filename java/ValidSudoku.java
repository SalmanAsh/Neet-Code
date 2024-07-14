import java.util.HashSet;

public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> seen = new HashSet<>();
        for (int i=0; i<board.length; i++){
            for (int j=0; j<board[i].length; j++){
                char value = board[i][j]; 
                if(value == '.') continue;
                if(!seen.add(value + "seen in row" + i)) return false;
                if(!seen.add(value + "seen in col" + j)) return false;
                if(!seen.add(value + "seen in box (" + i/3 + j/3 + ")")) return false;
            }
        }
        return true;
    }
}
