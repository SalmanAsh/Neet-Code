public class IntToRoman {
    public String solution(int num){
        int[] values = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        String[] roman = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"}; 
        String s = "";

        for (int i = roman.length - 1; i >= 0; i--){
            String r  = roman[i];
            int n = values[i];
            int count = num / n;
            while (count > 0){
                s += r;
                num -= n;
                count -= 1;
            }

        }

        return s;
    }
    
}
