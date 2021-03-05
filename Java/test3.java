import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;

public class test3 {
    public static void main(String[] args){
        OutputStream os= new BufferedOutputStream(new FileOutputStream("test.txt"));
    }
}
