import java.applet.Applet;
import java.awt.Graphics;
/*
<applet code="appletex.class" width="300" height="300"> 
</applet> 
*/

public class appletex extends Applet {
    @Override
    public void paint(Graphics g) {
        g.drawString("HI", 100, 100);
    }
}
