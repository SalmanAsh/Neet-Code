import java.util.Collections;
import java.util.HashMap;

public class LongestSubstringNoDuplicates {
    public int characterReplacement(String s, int k) {
        int l = 0;
        HashMap<Character, Integer> count = new HashMap<>();
        int res = 0;

        for (int r=0; r<s.length(); r++){
            if (count.containsKey(s.charAt(r))) count.put(s.charAt(r), count.get(s.charAt(r)) + 1);
            else count.put(s.charAt(r), 1);
            
            int value = Collections.max(count.values());
            while((r - l + 1) - value > k){
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1);
                l += 1;
            }

            res = Math.max(r - l + 1, res);
        }
        return res;
    }
}
