public class methover {

    public static int re(int x) {
        return x;
    }

    public static int re(int x, int y) {
        return x + y;
    }

    public static void main(String[] args) {
        System.out.println(re(5));
        System.out.println(re(3, 7));
        ex o = new ex();
        System.out.println(o.me());
        ex od = new ex(100);
        System.out.println(od.me());
    }
}

class ex {
    int x;

    ex() {
        this.x = 0;
    }

    ex(int a) {
        this.x = a;
    }

    public int me() {
        return this.x;
    }
}