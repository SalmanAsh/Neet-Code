import java.util.HashMap;
import java.util.Stack;

class ValidParanthesis{
    public boolean isValid(String s){
        if (s.length()%2 != 0) return false;
        Stack<Character> expected = new Stack<>();
        HashMap<Character, Character> match = new HashMap<>(3);
        match.put(')', '(');
        match.put(']', '[');
        match.put('}', '{');

        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(match.containsKey(c)){
                if(!expected.isEmpty() && match.get(c).equals(expected.peek())) expected.pop();
                else return false;
            }else expected.push(c);
        }
        return expected.isEmpty();

    }
}