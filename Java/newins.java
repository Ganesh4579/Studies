import java.lang.reflect.*;  
public class newins {
    public static void main(String[] a) throws ClassNotFoundException, InstantiationException, IllegalAccessException,
            NoSuchMethodException, SecurityException, IllegalArgumentException, InvocationTargetException {
        Class s=Class.forName("exz");
        exz e=(exz)s.newInstance();
        e.nw();
        System.out.println(int.class.getName());

        Class ee=exz.class;
        Object er=ee.newInstance();

        Method m=ee.getDeclaredMethod("mw",new Class[]{int.class});
        m.setAccessible(true);
        m.invoke(er,2);
        
        //

        Class[] c=new Class[]{int.class};
        System.out.println(c);
        System.out.println(new int[]{44,454}.length);
    }
}
class exz{
    void nw(){
        System.out.println("HI");
    }
    private void  mw(int x){
        System.out.println(x*x*x);
    }
}