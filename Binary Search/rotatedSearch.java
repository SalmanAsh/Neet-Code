public class rotatedSearch{
    public static void main(String[] args) {
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        System.out.println(search(nums));
        
    }
    public static int search(int[] nums){
        if (nums.length == 0) return -1;
        if (nums.length == 1) return nums[0];

        int l = 0;
        int r = nums.length - 1;

        while (l < r){
            int mid = l + (r - l) / 2;
            if (mid > 0 && nums[mid] < nums[mid - 1]){
                return nums[mid];
            }else if(nums[l] <= nums[mid] && nums[mid] > nums[r]){
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        return nums[l];
    }
}