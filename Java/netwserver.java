import java.io.*;  
import java.net.*;  

public class netwserver  {
    public static void main(String[] a)throws IOException{
        ServerSocket ss=new ServerSocket(8888);
        Socket s=ss.accept();
        DataInputStream d=new DataInputStream(s.getInputStream());
        String st=(String) d.readUTF();
        System.out.println(st);
        d.close();
        ss.close();
    }
}