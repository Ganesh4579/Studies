public class wrap {
    public static void main(String[] args) {
        j o = new j(2);
        System.out.println(o);
    }
}

class j {
    private int z;

    j() {
    };

    j(int x) {
        // this.z=x;
        z = x;
    }

    public String toString() {
        return Integer.toString(z);
    }
}