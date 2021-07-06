package com.test.Springproject;

import org.springframework.stereotype.Component;

@Component
public class bus implements vehicle {

	@Override
	public void drive() {
		System.out.println("Driving a bus");

	}

}
