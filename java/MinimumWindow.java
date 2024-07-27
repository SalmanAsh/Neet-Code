import java.util.HashMap;

public class MinimumWindow {
    public String minWindow(String s, String t) {
        if(t.equals("")) return "";
        HashMap<Character, Integer> countT = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();

        for (int i=0; i<t.length(); i++){
            if (countT.containsKey(t.charAt(i))) countT.put(t.charAt(i), countT.get(t.charAt(i)) + 1);
            else countT.put(t.charAt(i), 1);
        }

        int have = 0;
        int need = countT.size();
        int resLen = s.length() + 1;
        int[] res = {-1, -1};
        int l = 0;
        for(int i=0; i<s.length(); i++){
            if (window.containsKey(s.charAt(i))) window.put(s.charAt(i), window.get(s.charAt(i)) + 1);
            else window.put(s.charAt(i), 1);

            if (countT.containsKey(s.charAt(i)) && window.get(s.charAt(i)) == countT.get(s.charAt(i))) have++;
            while(have==need){
                if(i - l + 1 < resLen){
                    res[0] = l;
                    res[1] = i;
                    resLen = i - l + 1;
                }
    
                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                if (countT.containsKey(s.charAt(l)) && window.get(s.charAt(l)) < countT.get(s.charAt(l))) have--;
                l++;
            }
        }
        if (resLen != s.length() + 1) return s.substring(res[0], res[1] + 1);
        else return "";
    }
}
