package com.test.jdbctest;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class App {
  public static void main(String[] args) {
   try {
	   //Class.forName("com.mysql.jdbc.Driver");
	   Connection c=DriverManager.getConnection("jdbc:mysql://localhost:3306","root","Ganesh/4579");
	   Statement s=c.createStatement();
	   s.executeUpdate("USE base");
	   ResultSet r=s.executeQuery("SELECT * FROM employee");
	   
	   while(r.next()) {
		   System.out.println(r.getInt(1)+"\t"+ r.getString(2)+"\t"+ r.getString(3));
	   }
	   
   }
   catch (Exception e){
	   e.printStackTrace();
   }
  }
}

