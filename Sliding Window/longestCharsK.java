public class longestCharsK{
    public static void main(String args[]){
        String s = "ABBA";
        int k = 2;
        System.out.println(rep(s, k));
    }
    public static int rep(String s, int k){
        int max_length = 0;
        int l = 0;
        int n = s.length();
        int[] charCount = new int[26];
        int max_count = 0;

        for (int r = 0; r < n; r++){
            charCount[s.charAt(r) - 'A']++;
            max_count = Math.max(max_count, charCount[s.charAt(r) - 'A']);
            
            while ((r - l + 1 - max_count) > k){
                charCount[s.charAt(l) - 'A']--;
                l += 1;
            }
            max_length = Math.max(max_length, r - l + 1);
        }
        return max_length;
    }
}