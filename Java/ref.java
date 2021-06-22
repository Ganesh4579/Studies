class par{
    int a=100;
    static void foo(){
        System.out.println("par foo");
    }
    void boo(){
        System.out.println("par boo");
    }

}
class chi extends par{
    static void foo(){
        System.out.println("chi foo");
    }
    void boo(){
        System.out.println("chi boo");
    }
    public static void main(String a[]){
        par p=new chi();
        chi c=new chi();

        p.foo();
        c.foo();

        p.boo();
        c.boo();
        System.out.println(p.a);
        System.out.println(p.getClass());
     
    }

}