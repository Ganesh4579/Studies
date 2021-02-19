/**
 * 
 */
public class gene {
    public static <t> Object me(t a) {
        return a.getClass().getName();
    }

    /**
     * @param
     */
    public static void main(String[] args) {
        System.out.println(me(29));
        System.out.println(me(5.5455));
        System.out.println(me("fhgf"));
        exx<Integer> po = new exx<Integer>(20);

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