package com.test.springboot.emp;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class emps {

	@Autowired
	private empr er;
	
	public List<emp> getallemp() {
		List<emp> empall= new ArrayList<emp>();
		er.findAll().forEach(empall::add);
		return empall;
	}

	public emp getemp(int b) {
		// TODO Auto-generated method stub
		return null;
	}

	public void addemp(emp e) {
		 er.save(e);
		
	}

	public void updateemp(int b, emp e) {
		// TODO Auto-generated method stub
		
	}

	public void deleteemp(int b) {
		// TODO Auto-generated method stub
		
	}
	
}
