import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexx {
    public static void main(String[] args) throws ArithmeticException{
        Pattern p = Pattern.compile("Hello world",Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher("Hi Hello World");
        boolean f=m.find();
        if(f) {
            System.out.println("Match found");
          } else {
            System.out.println("Match not found");
          }
          throw new ArithmeticException("occured");
    }

}