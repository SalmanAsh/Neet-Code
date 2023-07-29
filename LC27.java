public class LC27 {
    public int removeElement(int[] nums, int val){
        if (nums.length == 0) return 0;

        int valid_num = 0;
        for(int i = 0; i < nums.length; i++){
            int n = nums[i];
            if(n != val){
                nums[valid_num] = n;
                valid_num++;
            }
        }
        return valid_num;
    }
}
