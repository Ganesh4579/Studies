import java.io.File; // Import the File class
import java.io.IOException; // Import the IOException class to handle errors
import java.util.Queue;
import java.util.LinkedList;

public class test1 {
  public static void main(String[] args) throws IOException {
    File o = new File("filename.txt");
    System.out.println(o.createNewFile());
    //
    // System.exit(1);
    Queue<Integer> l = new LinkedList<Integer>();
    System.out.println(l.getClass().getName());

    //

    // SBI s = (SBI)new Bank();
    ICICI i = new ICICI();
    AXIS a = new AXIS();
    // System.out.println("SBI Rate of Interest: " + s.getRateOfInterest());
    System.out.println("ICICI Rate of Interest: " + i.getRateOfInterest());
    System.out.println("AXIS Rate of Interest: " + a.getRateOfInterest());
    System.out.println(i.getClass().getName());
    System.out.println(i.hashCode());
    System.out.println(i.toString());
  }
}

class Bank {
  int getRateOfInterest() {
    return 0;
  }
}

// Creating child classes.
class SBI extends Bank {
  int getRateOfInterest() {
    return 8;
  }
}

class ICICI extends Bank {
  int getRateOfInterest() {
    return 7;
  }
}

class AXIS extends Bank {
  int getRateOfInterest() {
    return 9;
    /*
     * try { int a[] = new int[5]; a[5] = 30 / 0; } /* catch (Exception e) {
     * System.out.println("common task completed"); }
     */

    // Exception should be in last

    // Newsted try can be posssible like if else
    /*
     * catch (ArithmeticException e) { System.out.println("task1 is completed"); }
     * catch (ArrayIndexOutOfBoundsException e) {
     * System.out.println("task 2 completed"); }
     */
  }
}