import java.io.*;  
import java.net.*;  

public class netwwwclient {
    public static void main(String[] a)throws IOException{
        Socket s=new Socket("localhost",8888);
        DataOutputStream d=new DataOutputStream(s.getOutputStream());
        d.writeUTF("HI");
        d.flush();
        d.close();
        s.close();
    }
}
