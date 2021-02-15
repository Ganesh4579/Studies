public class encap {

    public static void main(String args[]) {
        ex1 o1 = new ex1();
        o1.m1(5);
        System.out.println(o1.m2());

    }

}

class ex1 {
    private int x;

    void m1(int a) {
        this.x = a;
    }

    int m2() {
        return this.x;
    }
}