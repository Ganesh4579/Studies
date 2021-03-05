public class core3 {
    public static void main(String args[]) throws InterruptedException {
        //new B1().get().message();
        A h=new B1();
        System.out.println(h.get());
        Thread.sleep(10000);
    }
}

class A {
    A get() {
        return this;
    }
}

class B1 extends A {
    B1 get() {
        return this;
    }

    void message() {
        System.out.println("welcome to covariant return type");
    }
}