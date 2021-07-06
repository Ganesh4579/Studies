package com.test.SpringAOP;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.test.SpringAOP.service.shape;

public class App {
  public static void main(String[] args) {
    ApplicationContext f=new ClassPathXmlApplicationContext("config.xml");
    shape s= f.getBean("shape",shape.class);
    System.out.println(s.getC().getName());
  }
}
 