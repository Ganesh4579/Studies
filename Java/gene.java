import java.io.IOException;

/**
 * 
 */
public class gene {
    public static <t,y> Object me(t a,y b) {
        return a.getClass().getName();
    }

    /**
     * @param
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        System.out.println(me(29,45));
        System.out.println(me(5.5455,"hjh"));
        System.out.println(me("fhgf",7));
        exx<Integer> po = new exx<Integer>(20);
        System.out.println(Runtime.getRuntime().exec("clear"));
        System.out.println(Runtime.getRuntime().availableProcessors());

    }

}

class exx<x> {
    x a;

    exx(x w) {
        this.a = w;
        System.out.println(this.a);
        System.out.println(this.a.getClass().getName());
    }
}