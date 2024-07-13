public class ProductSelf {
    public int[] productExceptSelf(int[] nums) {
        int l = 0;
        int r = 0;
        int[] res = new int[nums.length];

        for (int i = 0; i < res.length; i++) res[i]=1; 

        while (l < nums.length){
            if(l == r) r+=1;
            if(r == nums.length){
                l += 1;
                r = 0;
            }else{
                res[l] *= nums[r];
                r+=1;
            }
        }
        return res;
    }
}
