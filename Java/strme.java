import java.util.StringTokenizer;

public class strme {
    public static void main(String[] args){
        String s="Hello World";


        //System.out.println(s.charAt(4));
        //System.out.println(s.codePointAt(4));
        
        //

        String a="Hello",b="World";
        System.out.println(a.concat(b));
        System.out.println(a.equals(b));
        System.out.println(a==(b));
        System.out.println(a.compareTo(b));
        System.out.println(a.substring(2,4));

        //
        System.out.println("\n\n\n");

        StringBuffer sb=new StringBuffer("Hello");
        StringBuffer sb1 = new StringBuffer();
        StringBuffer sb2=new StringBuffer(4);

        System.out.println(sb2);
        sb1.append("Hello World");
        System.out.println(sb1);

        StringBuilder sbr=new StringBuilder("Java");
        StringBuilder sbr1=new StringBuilder();
        StringBuilder sbr2=new StringBuilder(4);

        //

        StringTokenizer t =new StringTokenizer(String.valueOf(sb1)," ");
        System.out.println(t);
        while(t.hasMoreTokens()){
            System.out.println(t.nextToken());
        }
        String v=String.valueOf(sb1);

        System.out.println(v.contains("lo"));
        System.out.println(v.intern());

        System.out.println(String.join(":",a,b));
    }
}
