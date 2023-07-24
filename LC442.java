import java.util.HashSet;
import java.util.ArrayList;
import java.util.List;

public class LC442 {
    public List<Integer> findDuplicates(int[] nums){
        HashSet<Integer> seen = new HashSet<>();
        ArrayList<Integer> duplicates = new ArrayList<>();

        for (int n: nums){
            if (seen.contains(n) )duplicates.add(n);
            else seen.add(n);
        }

        return duplicates;

    }
    
}
