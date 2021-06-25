public class testsuper extends sup{
    testsuper(){
    	super();
    	System.out.println("child");
    }
    public static void main(String[] a){
    	new testsuper();
    }
}


class sup{
    sup(){
        System.out.println("super");
    }
}
