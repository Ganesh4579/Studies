import java.io.*;  
import java.net.*;  

public class exURL {
    public static void main(String a[]) throws IOException {
        //URL u=new URL("https://www.google.com/");
        URLConnection uc=new  URL("https://www.google.com/").openConnection();
        InputStream i=uc.getInputStream();
        int n;
        while((n=i.read()) != -1){
            //System.out.print(n);
        }
        System.out.println((22e3d+"\n"+"dfdsf"));
    }
}
