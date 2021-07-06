package com.test.Springproject;

public class truck implements vehicle{
	private String t;
	private engine e;
	public engine getE() {
		return e;
	}
	public void setE(engine e) {
		this.e = e;
	}
	truck(String a){
		this.t=a;
	}
	public void drive() {
		System.out.println("Driving a truck");
		System.out.println(t);
		System.out.println(e.getModel());
	}
}
