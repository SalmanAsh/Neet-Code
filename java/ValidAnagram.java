import java.util.HashMap;

class ValidAnagram{
    public boolean solution(String s, String t){
        if (s.length() != t.length()){
            return false;
        }
        int[] chars = new int[26];
        for (int i = 0; i < s.length(); i++){
            chars[s.charAt(i) - 'a']++;
            chars[t.charAt(i) - 'a']--;
        }

        for (int n: chars){
            if (n != 0) return false;
        }
        return true;
    }

    public boolean solution2(String s, String t){
        if (s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> charS = new HashMap<>();
        HashMap<Character, Integer> charT = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            if(charS.containsKey(s.charAt(i))){
                charS.put(s.charAt(i), charS.get(s.charAt(i)) + 1);
            }else{
                charS.put(s.charAt(i), 1);
            }
            
            if(charT.containsKey(t.charAt(i))){
                charT.put(t.charAt(i), charT.get(t.charAt(i)) + 1);
            }else{
                charT.put(t.charAt(i), 1);
            }
        }

        for (char c: charS.keySet()){
            if(!charT.containsKey(c)) return false;
            else if(charS.get(c) != charT.get(c)) return false;
        }
        return true;
    }
}