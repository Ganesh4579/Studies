import java.util.ArrayList;
import java.util.Iterator;

public class iter {
    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            l.add(i);
        }
        Iterator<Integer> it = l.iterator();
        System.out.println(it);
        System.out.println(it.next());
        System.out.println(it.next()+"\n");  
        while(it.hasNext()) {
            System.out.println(it.next());
          }
    }
}