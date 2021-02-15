public class recur {
    public static int recfunc(int x) {
        if (x < 0) {
            return 0;
        } else {
            return x + recfunc(x - 1);
        }
    }

    public static void main(String arg[]) {
        System.out.println(recfunc(3));
    }
}