import java.util.HashSet;


class ContainsDuplicates{
    public boolean solution(int[] num){
        HashSet<Integer> seen = new HashSet<Integer>();

        for (int n:num){
            if(seen.contains(n)){
                return true;
            }
            seen.add(n);
        } 
        return false;
    }
}