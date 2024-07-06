class ValidPalindrome{
    public boolean isPalindrome(String s){
        int l = 0;
        int r = s.length() - 1;

        while (l <= r){
            if (!(Character.isLetterOrDigit(s.charAt(l)))){
                l += 1;
            }else if (!(Character.isLetterOrDigit(s.charAt(r)))) {
                r -= 1;
            }else if (Character.toLowerCase(s.charAt(r)) != Character.toLowerCase(s.charAt(l))){
                return false;
            }else{
                l += 1;
                r -= 1;
            }
        }
        return true;
    }
}