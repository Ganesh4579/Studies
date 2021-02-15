public class inter implements in1 {
    public void hi() {
        System.err.println(true);
    }

    public static void main(String[] args) {
        inter o1 = new inter();
        o1.hi();
        System.out.println("o1.x");

    }

}

interface in1 {

    public int x = 10;

    public void hi();

}