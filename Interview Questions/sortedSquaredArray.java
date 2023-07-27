import java.util.Arrays;

public class sortedSquaredArray {
    public static void main(String[] args) {
        int[] arr = {-3, -2, -1};
        arr = solution2(arr);
        for (int a: arr){
            System.out.println(a);
        }
    }
    // Simple but inefficient solution   O(NlogN)
    public static int[] solution(int[] array){
        int[] squared = new int[array.length];
        for(int i = 0; i < array.length; i++){
            squared[i] = array[i] * array[i];
        }
        Arrays.sort(squared);
        return squared;
    }

    // Linear time solution   O(N)
    public static int[] solution2(int[] array){
        int[] result = new int[array.length];
        int left = 0;
        int right = array.length - 1;
        for(int i = array.length - 1; i >= 0; i--){
            if(Math.abs(array[left]) > array[right]){
                result[i] = array[left] * array[left];
                left++;
            }else{
                result[i] = array[right] * array[right];
                right--;
            }
        }
        return result;
    }
}
