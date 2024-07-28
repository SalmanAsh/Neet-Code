import java.util.ArrayList;
import java.util.List;

public class CombinationSum {
    public  List<List<Integer>> solution(int[] nums, int target){
        List<List<Integer>> res =  new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList();
        dfs(nums, 0, cur, res, 0, target);
        return res;
    }

    public void dfs(int[] nums, int i, List<Integer> cur, List<List<Integer>> res, int total, int target){
        if(total == target) {
            res.add(new ArrayList(cur));
        }else if(total > target || i >= nums.length) return;
        else{
            cur.add(nums[i]);
            dfs(nums, i, cur, res, total + nums[i], target);
            cur.remove(cur.get(cur.size() - 1));
            dfs(nums, i + 1, cur, res, total, target);
        }
    }

}
