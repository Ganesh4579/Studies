import java.io.*;
import java.time.Clock;

class M{  
 void method()throws IOException{ 
  //throw new IOException("device error");  
 }  
 void m(){//throws ArithmeticException{  
    //throw new ArithmeticException("sorry");  
    }  
}  
class test2{  
   public static void main(String args[])throws IOException{//declare exception  
     M m=new M();  
     m.method();
     m.m();  
  
    System.out.println("normal flow...");  
    System.out.println(Clock.systemUTC().getZone());
  }  
}  