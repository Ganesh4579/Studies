import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class serializ {
    public static void main(String[] a) throws FileNotFoundException, IOException, ClassNotFoundException {
        FileOutputStream f = new FileOutputStream("test1.txt");
        ObjectOutputStream o = new ObjectOutputStream(f);

        o.writeObject(new ed(1001, "Hari"));
        o.flush();
        o.close();

        ObjectInputStream i = new ObjectInputStream((new FileInputStream("test1.txt")));
        ed ed1 = (ed) i.readObject();
        System.out.println(ed1.name + "   " + ed1.id);
    }
}

class ed implements Serializable {
    /**
     *
     */
    private static final long serialVersionUID = 1L;
    int id;
    String name;

    ed(int i, String n) {
        id = i;
        name = n;
    }
}