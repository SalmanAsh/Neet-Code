import java.util.HashSet;

public class sudoku2 {
    public boolean validSudoku(char[][] grid){
        HashSet<String> seen = new HashSet<>();

        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                if(grid[i][j] != '.'){
                    String row = "found " + grid[i][j] + " in row " + i;
                    String col = "found " + grid[i][j] + " in col " + j;
                    String box = "found " + grid[i][j] + " in box " + i/3 + "-" + j/3;
                    if (seen.contains(row) || seen.contains(col) || seen.contains(box)) return false;
                    seen.add(row);
                    seen.add(col);
                    seen.add(box);
                }
            }
        }
        return true;
    }
}
