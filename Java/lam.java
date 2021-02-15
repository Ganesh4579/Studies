import java.util.ArrayList;
interface a{
    void s();
}

public class lam {
  public static void main(String[] args) {
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(5);
    numbers.add(9);
    numbers.add(8);
    numbers.add(1);
    numbers.forEach( (n) -> { System.out.println(n); } );
    int z=2;
    //System.out.println((z)->{z+7;}); //(argument-list) -> {body} 
    a ir=new a(){
        public void s(){
            System.out.println("hi"); //Anonymous inner class  
        }
    };
    ir.s(); 
  }
}