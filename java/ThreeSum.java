import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        LinkedList<List<Integer>> sol = new LinkedList<List<Integer>>();
        for (int i=0;i<nums.length - 2; i++){
            int n = nums[i];
            if (i > 0 &&  n == nums[i - 1]) continue;
            int target = -n;
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right){
                int num1 = nums[left];
                int num2 = nums[right];
                if (num1 + num2 == target){
                    ArrayList<Integer> res = new ArrayList<>();
                    res.add(n);
                    res.add(num1);
                    res.add(num2);
                    sol.add(res);
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                }
                if(num1 + num2 < target) left += 1;
                else right -= 1;

            }
        }
        return sol;
    }
}
