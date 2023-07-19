import java.util.HashMap;

public class firstNonRepeatingChar{
    public static void main(String[] args) {
        
    }

    public char linear(String s){
        HashMap<Character, Integer> count = new HashMap<>();
        for (int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            if(count.containsKey(c)) count.put(c, count.get(c) + 1);
            else count.put(c, 1);
        }

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (count.get(c) == 1) return c;
        }
        return '_';
    }

    /*
     * O(n^2) Solution. Very slow. Not good enough for big companies.
     */
    public char quadraticSol(String str){
        for (int i = 0; i < str.length(); i++){
            for (int j = 0; j < str.length(); j++){
                if (str.charAt(i) == str.charAt(j) && (i != j)){
                    return str.charAt(i);
                }
            }
        }
        return '_';
    }
}