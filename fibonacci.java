public class fibonacci{
    private static long[] fibCache;
    public static void main(String[] args){
        int n = 100;
        fibCache = new long[n+1];
        System.out.println(fib(n));
    }
    public static long fib(int n){
        if(n<=1){
            return n;
        }
        if(fibCache[n] != 0){
            return fibCache[n];
        }
        long nthFib =fib(n-1) + fib(n-2);
        fibCache[n] = nthFib;
        return nthFib;
    }
}