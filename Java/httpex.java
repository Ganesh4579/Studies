
import java.io.*;    
import java.net.*;    
public class httpex {
    public static void main(String[] args) throws MalformedURLException,IOException {
        URL u=new URL("http://www.javatpoint.com/java-tutorial");
        HttpURLConnection uh= (HttpURLConnection) u.openConnection();
        for (int i=0; i< 10; i++){
            System.out.println(uh.getHeaderFieldKey(i)+"  : "+uh.getHeaderField(i));
        }
        uh.disconnect();
    }
}
