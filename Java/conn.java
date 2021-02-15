class conn
{
    public static void main(String arg[])
    {
     ou: for (int i=0;i<10;i++)
     {
      for (int j=0;j<10;j++)
      {
       if(j>i)
{
    System.out.println();
       continue ou;
    }



    System.out.print((i*j)+" ");
}
     }
    
}
}