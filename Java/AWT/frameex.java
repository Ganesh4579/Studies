import java.awt.*;
import java.awt.event.*;

public class frameex extends Frame implements ActionListener{
    TextField t;
    Button b;
    Label l;
    frameex() {
        l=new Label();
        l.setBounds(50,100, 250,20);      
        add(l);
        t=new TextField();
        add(t);
        t.setBounds(60,50,170,20);  
        b = new Button("CLICK");
        b.setBounds(50, 50, 50, 50);
        add(b);
        b.addActionListener(this);
        setSize(400, 400);
        setLayout(null);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent a){
        t.setText("HI");
       try{
        l.setText(java.net.InetAddress.getByName("localhost").getHostAddress());
       }
       catch (Exception e){
           e.printStackTrace();
       }
    }

    public static void main(String... args) {
        new frameex();
    }
}