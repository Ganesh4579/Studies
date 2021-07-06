package com.test.springboot.emp;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class empc {
	
	@Autowired
	private emps empservice;
	
	@RequestMapping("/emp")
	public List<emp> empdetails(){
		return empservice.getempdetails();
	}
	
	@RequestMapping("/emp/{id}")
	public emp singleempdetail(@PathVariable("id") int b) {
		return empservice.getbyid(b);
	}
	
	@RequestMapping(method=RequestMethod.POST , value="/emp")
	public void addemp(@RequestBody emp e) {
		 empservice.addemp(e);
	}
	
	@RequestMapping(method=RequestMethod.PUT ,value= "/emp/{id}")
	public void updateemp(@PathVariable("id") int b , @RequestBody emp e) {
		empservice.updateemp(b,e);
	}
	
	@RequestMapping(value="/emp/{id}",method=RequestMethod.DELETE)
	public void deleteemp(@PathVariable("id") int b ) {
		empservice.deleteemp(b);
	}
}
