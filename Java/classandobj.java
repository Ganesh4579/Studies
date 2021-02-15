public class classandobj {
    public static void main(String[] args) {
        c1 o1 = new c1(10);
        c2 o2 = new c2();
        System.out.println(o1.a + "\n" + o1.c);
        System.out.println(o2.a + "\n" + o2.b);

    }

}

class c1 {
    int a = 1;
    int c;

    public c1(int x) {
        c = x;
    }
}

class c2 {
    int a = 2;
    int b;

    public c2() {
        b = 3;
    }

}