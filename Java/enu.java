public class enu {
    enum na {
        l, M, h
    }

    public static void main(String a[]) {
        na v1 = na.M;
        System.out.println(v1);
        System.out.println(na.h);
        System.out.println(na.values());
        System.out.println(na.valueOf("M"));
        System.out.println(v1.ordinal());
        for (na v2 : na.values()) {
            System.out.println(v2);
        }

    }
}
