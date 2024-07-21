public class TwoSum {
    public int[] twoSum(int[] nums, int target){
        int left = 0;
        int right = nums.length - 1;
        int[] res = new int[2];
        while (left < right){
            int num1 = nums[left];
            int num2 = nums[right];
            if (num1 + num2 == target){
                res[0] = left + 1;
                res[1] = right + 1;
                break;
            }
            if(num1 + num2 < target) left += 1;
            else right -= 1;

        }
        return res;
    }
    
}
