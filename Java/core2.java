import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Date;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;

public class core2 {
    public static void main(String[] a) throws IOException, ParseException {
        FileWriter w = new FileWriter("test.txt");
        w.write("sadsafdsfsff");
        w.flush();
        java.io.FileReader f = new FileReader("test.txt");
        Scanner b = new Scanner(f);
        String wq = b.nextLine();
        System.out.println(wq);

        aq xx = new aq();

        System.out.println(xx.we);
        xx.we = 45;
        System.out.println(xx.we);

        //

        String sg = "Thu, Dec 31 1998 23:37:50";
        java.util.Date d = new SimpleDateFormat("E, MMM dd yyyy HH:mm:ss").parse(sg);
        System.out.println(d);

    }

}

class aq {
    int we = 21;
}