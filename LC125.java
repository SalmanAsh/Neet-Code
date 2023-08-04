public class LC125 {
    public boolean isPalindrome(String s){
        String fixed_string = "";

        for(char c: s.toCharArray()){
            if (Character.isDigit(c) || Character.isLetter(c)) fixed_string += c;
        }
        
        fixed_string = fixed_string.toLowerCase();
        int l = 0;
        int r = fixed_string.length() - 1;
        while(l <= r){
            if(fixed_string.charAt(l) != fixed_string.charAt(r)) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}
