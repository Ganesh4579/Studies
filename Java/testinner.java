

public class testinner{
    public static void main(String ar[]){

        outer o=new outer();
        System.out.println(new outer.inner().b);
    }
}


class outer{
    int a=2;
    static class inner {
        int b=3;
    } 
}