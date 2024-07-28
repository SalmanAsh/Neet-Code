import java.util.HashSet;

public class SearchWord {
    public boolean exist(char[][] board, String word) {
        int ROWS = board.length;
        int COLS = board[0].length;
        HashSet<String> path = new HashSet<>();

        for (int i=0; i<ROWS; i++){
            for (int j=0; j < COLS; j++){
                if (dfs(board, word, i, j, 0, path) == true) return true;
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, String word, int r, int c, int i, HashSet<String> path){
        if(i == word.length()) return true;
        if(r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i) || path.contains("row: " + r + "col: " + c))return false;

        path.add("row: " + r + "col: " + c);
        boolean res = dfs(board, word, r + 1, c, i + 1, path) || dfs(board, word, r, c + 1, i + 1, path) ||
        dfs(board, word, r - 1, c, i + 1, path) || dfs(board, word, r, c - 1, i + 1, path);
        path.remove("row: " + r + "col: " + c);

        return res;
    }
}
