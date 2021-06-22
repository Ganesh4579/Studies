import java.util.ArrayList;

public class arrlist {
    public static void main(String[] args) {
        ArrayList<Integer> mylist = new ArrayList<Integer>();
        for (int i = 0; i <= 10; i++) {
            mylist.add(i);
        }
        System.out.println(mylist);
        mylist.set(0,100);
        System.out.println(mylist.get(0)+"/n/n/n");

        System.out.println(34.344343f );
        System.out.println(34222222d );
        System.out.println("\\" );
    }
}