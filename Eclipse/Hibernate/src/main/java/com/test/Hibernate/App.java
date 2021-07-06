package com.test.Hibernate;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.service.ServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;


public class App {
  public static void main(String[] args) {
    
	  Name n=new Name();
	  n.setFname("Thanushree");
	  n.setLname("papa");
	  
	  
	  Name nn=new Name();
	  nn.setFname("Thoppa");
	  nn.setLname("papa");
	  
	  
	  
	  school ss=new school();
	  ss.setMark(90);
	  ss.setRole("good");
	  ss.setRollnum(101);
	  
	  home h=new home();
	  h.setId(1005);
//	  h.setName(n);
	  h.setAge(0);
	  h.setRole("Baby");
	  h.getNames().add(n);
	  h.getNames().add(nn);
	  
//	
//	  h.setS(ss);
	  
//	  
//	  employee e=new employee();
//	  e.setEmpid(1001);
//	  e.setName("Govind");
//	  e.setSalary(30000);
//	  
	  
//	  e.getSet().add("HI");
//	  e.getSet().add("GOOD");
//	  e.getSet().add("MORNING");
//	  e.getSet().add("MAN");
//	  e.getSet().add("OOH!");
//	  
//	  
//	  branch b=new branch();
//	  b.setBranchid(12);
//	  b.setBranchname("Chennai");
//	  
//	  e.setBranch(b);
	  
	  SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(home.class).addAnnotatedClass(Name.class).buildSessionFactory();
	  
	  Configuration c=new Configuration().configure("hibernate.cfg.xml"); //.addAnnotatedClass(home.class);
//	  ServiceRegistry sr= new StandardServiceRegistryBuilder().applySettings(c.getProperties()).build();
//	  SessionFactory sf=c.buildSessionFactory((new StandardServiceRegistryBuilder().applySettings(c.getProperties()).build()));
	  
	  Session s=sf.openSession();
//	  Transaction t=s.beginTransaction(); //s.getTranscation();
	  s.beginTransaction();
	  s.save(h);
//	  s.save(s);
	  s.getTransaction().commit();
//	  t.commit();
	  
//	  home h=s.get(home.class,1001);
//	  System.out.println(h);
	  s.close();
	  s.close();
  }
}
