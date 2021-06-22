import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class filehand {
    public static void main(String a[]) {
        try {
            File f = new File("test.txt");
            FileWriter w = new FileWriter("test11.txt");
            Scanner r = new Scanner(f);
            if (f.createNewFile()) {
                System.out.println("File created: " + f.getName());

            } else {
                System.out.println("File already exists.");
                w.write("Welcome");
                w.close();
                System.out.println("Successfully wrote to the file.");
                while (r.hasNextLine()) {
                    System.out.println(r.nextLine());
                }
                if (f.delete()) {
                    System.out.println("Deleted the file: " + f.getName());
                } else {
                    System.out.println("Failed to delete the file.");
                }
                r.close();
            }

        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
       
    }
}
