public class anonyminner {
    public static void main(String argv[]) {
        te t = new te() {
            @Override
            void msg() {
                System.out.println("HI");
            }
        };
        t.msg();

        s k = new s() {
            @Override
            public void msg1() {
                System.out.println("WELCOME");
            }
        };
        k.msg1();
    }
}

abstract class te {
    abstract void msg();
}

interface s {
    void msg1();
}