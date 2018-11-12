/**
 * Created by yksu on 2018-04-10.
 */
public class Recursion {
    public static void main(String[] args) {
        System.out.println("0! = " + fact(0));
        System.out.println("1! = " + fact(1));
        System.out.println("2! = " + fact(2));
        System.out.println("3! = " + fact(3));
        System.out.println("4! = " + fact(4));

        System.out.println("fib(1) = " + fib(1));
        System.out.println("fib(2) = " + fib(2));
        System.out.println("fib(3) = " + fib(3));
        System.out.println("fib(4) = " + fib(4));
        System.out.println("fib(5) = " + fib(5));
    }
    static int fact(int n){
        // assuming that n is a positive integer or 0
        if (n >= 1) { return n * fact(n - 1); }
        else { return 1; }
    }

    static int fib(int n){
        // assuming that n is a positive integer
        if (n >= 3) { return fib(n-1) + fib(n-2); }
        else { return 1; }
    }
}
