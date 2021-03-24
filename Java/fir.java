import pac.*;
import java.util.Scanner;
import java.util.logging.LogManager;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class fir {
    public static void main(String[] a)

    {
        Scanner in = new Scanner(System.in);
        int x = 10;
        System.out.println("Hello World");
        System.out.println(String.format("%d", x)); // string interpolation is not possible whereas formatting is
        System.out.println("Enter name");
        String name = in.nextLine();
        in.close();
        System.out.println(String.format("%s", name));

        LocalDateTime dat = LocalDateTime.now();
        System.out.println(dat);

        DateTimeFormatter dat1 = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String dat2 = dat.format(dat1);
        System.out.println(dat2);
        System.out.println(dat2.getClass());
        //in1 ob =new in1();
        //System.out.println(ob.xxx);
        System.out.println(pac.getName());
        //LogManager.log("My Message");

    }
}