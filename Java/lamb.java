public class lamb {
    interface c {
        public void cq(int a);
    }

    public static void main(String args[]) {
        c obj = (int a) -> {
            System.out.println(a);
            a = a + 23445;
            System.out.println(a);
        };
        obj.cq(2);
    }
}
