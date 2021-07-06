package com.test.Springproject;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class van implements vehicle {
	
	@Autowired
	private engine e;

	public engine getE() {
		return e;
	}

	public void setE(engine e) {
		this.e = e;
	}

	@Override
	public void drive() {
		System.out.println("Driving a van");
		System.out.println("engine"+e.getModel());
	}

}
	