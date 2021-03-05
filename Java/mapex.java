import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class mapex {
    public static void main(String a[]) {
        Map<Integer, String> m = new HashMap<Integer, String>();
        m.put(1, "a");
        m.put(2, "b");
        m.put(3, "c");

        System.out.println(m);
        System.out.println(m.get(2));

        Set s = m.entrySet();
        Iterator i = s.iterator();

        System.out.println(s);

        while (i.hasNext()) {
            Map.Entry e = (Map.Entry) i.next();
            System.out.println(e.getKey());
            System.out.println(e.getValue());
            System.out.println(e.hashCode());
        }

        TreeMap<Integer, String> map = new TreeMap<Integer, String>();
        map.put(110, "Amit");
        map.put(102, "Ravi");
        map.put(101, "Vijay");
        map.put(103, "Rahul");

        for (Map.Entry mx : map.entrySet()) {
            System.out.println(mx.getKey() + " " + mx.getValue());

        }
    }
}