import java.util.HashSet;

public class LongestSubstringNoRep {
    public int lengthOfLongestSubstring(String s){
        int l= 0;
        int r;
        int res = 0;
        HashSet<Character> chars = new HashSet<>();
        for (r = 0; r < s.length(); r++){
            while (chars.contains(s.charAt(r))) {
                chars.remove(s.charAt(l));
                l += 1;
            }
            chars.add(s.charAt(r));
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
