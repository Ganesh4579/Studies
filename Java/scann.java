import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class scann {
    public static void main(String a[]) {
        Scanner s = new Scanner(System.in);
        int x = s.nextInt();
        System.out.println(x);
        s.close();

        //
        LocalDateTime l = LocalDateTime.now();
        System.out.println(l);
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        String sq = l.format(f);
        System.out.println(sq);
    }
}
