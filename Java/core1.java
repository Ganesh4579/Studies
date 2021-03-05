import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.Scanner;

public class core1 {
    public static void main(String ar[]) throws IOException,NumberFormatException {
        char a='w',b='f';
        int c=a+b;
        System.out.println(c);
        //newLine();   * private method 
        //java.io.PrintStream.println(c);
        System.out.println(String.valueOf(c));
        //System.out.println(Integer.parseInt(a));
        
        
        //

        InputStreamReader r=new InputStreamReader(System.in);
        BufferedReader ww=new BufferedReader(r);
        String s= ww.readLine();
        System.out.println(s);

        //

        Scanner ss=new Scanner(System.in);

    }
}
