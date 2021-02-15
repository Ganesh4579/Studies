public class enu {
    enum na {
        l, m, h
    }

    public static void main(String a[]) {
        na v1 = na.m;
        System.out.println(v1);
        for (na v2 : na.values()) {
            System.out.println(v2);
        }

    }
}
