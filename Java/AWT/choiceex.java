import java.awt.*;
import java.awt.event.*;

public class choiceex {
    choiceex() {
        Frame f = new Frame();
        Label l = new Label();
        l.setSize(400, 100);
        l.setAlignment(Label.CENTER);
        Button b = new Button("SHOW");
        b.setBounds(200, 100, 50, 20);

        Choice c = new Choice();
        c.setBounds(100, 100, 75, 75);
        c.add("JAVA");
        c.add("C");
        c.add("C++");
        c.add("PYTHON");
        f.add(c);
        f.add(b);
        f.add(l);
        f.setSize(400, 400);
        f.setLayout(null);
        f.setVisible(true);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                l.setText(c.getItem(c.getSelectedIndex()));
            }
        });
    }

    public static void main(String[] a) {
        new choiceex();
    }
}
