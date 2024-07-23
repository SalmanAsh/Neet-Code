public class TrapRainWater {
    public int trap(int[] height){
        if (height.length == 0) return 0;
        int l = 0;
        int r = height.length - 1;
        int leftMax = 0;
        int rightMax = 0;
        int res = 0;
        while (l < r){
            if (leftMax < rightMax){
                l += 1;
                leftMax = Math.max(height[l], leftMax);
                res += leftMax - height[l];
            }else{
                r -= 1;
                rightMax = Math.max(height[r], rightMax);
                res += rightMax - height[r];
            }

        }
        return res;
    }
}   
