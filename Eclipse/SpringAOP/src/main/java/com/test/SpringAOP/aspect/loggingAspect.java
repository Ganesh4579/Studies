package com.test.SpringAOP.aspect;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class loggingAspect {
	
//	@Before("within(com.test.SpringAOP.model.*)")
//	public void advice() {
//		System.out.println("Welcome");
//	}
	
	
	@Before("execution(public String com.test.SpringAOP.model.circle.getName())")
	public void advice() {
		System.out.println("Welcome");
	}
}
