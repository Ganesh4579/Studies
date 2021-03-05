public class enumex {
    public enum comp {
        mouse, keyboard, monitor
    }

    public static void main(String[] args) {
        for (comp s : comp.values()) {
            System.out.println(s);
        }
        System.out.println(comp.valueOf("mouse"));
        System.out.println(comp.valueOf("monitor").ordinal());
        comp c = comp.mouse;
        System.out.println(c);

        for (season s : season.values()) {
            System.out.println(s);
            System.out.println(s.v);
        }
    }
}

enum season {
    WINTER(5), SPRING(10), SUMMER(15), FALL(20);

    int v;

    private season(int a) {
        this.v = a;
    }
}