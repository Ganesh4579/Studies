package com.test.Springproject;

import java.util.List;

public class car implements vehicle{
	private String s;
	private List<String> parts;
	public List<String> getParts() {
		return parts;
	}
	public void setParts(List<String> parts) {
		this.parts = parts;
	}
	public String getS() {
		return s;
	}
	public void setS(String s) {
		this.s = s;
	}
	public void drive() {
		System.out.println("Driving a car");
		System.out.println(s);
		for (String p:parts) {
			System.out.println("Part :"+p);
		}
	}
}
 