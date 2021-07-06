package com.test.Springproject;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class App {
  public static void main(String[] args) {
    //ApplicationContext f=new ClassPathXmlApplicationContext("conf.xml");
	  
	AbstractApplicationContext f=new ClassPathXmlApplicationContext("conf.xml");
    f.registerShutdownHook();
    vehicle v=(vehicle) f.getBean("van");
    v.drive();
  }
}
 		