public class MostWater {
    public int solution(int[] heights){
        int l = 0;
            int r = heights.length - 1;
            int res = 0;
            while (l < r){
                int base = r - l;
                int height = Math.min(heights[r], heights[l]);
                res = Math.max(base*height, res);
                if (heights[r] < heights[l]) r--;
                else l++;
            }
            return res;
    }
}
