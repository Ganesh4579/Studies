package com.test.Springproject;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

public class bike implements vehicle,InitializingBean ,DisposableBean{
	
	private int a;
	public int getA() {
		return a;
	}


	public void setA(int a) {
		this.a = a;
	}


	public int getB() {
		return b;
	}


	public void setB(int b) {
		this.b = b;
	}


	public int getC() {
		return c;
	}


	public void setC(int c) {
		this.c = c;
	}


	private int b;
	private int c;
	
	
	@Override
	public void drive() {
		System.out.println("Riding a bike");
		System.out.println(a+"\n"+b+"\n"+c+"\n");
	}


	@Override
	public void destroy() throws Exception {
		System.out.println("Bike get stopped");
		
	}


	@Override
	public void afterPropertiesSet() throws Exception {
		System.out.println("Bike get started");
		
	}

}
