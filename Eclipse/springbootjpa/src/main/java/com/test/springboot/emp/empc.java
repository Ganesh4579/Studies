package com.test.springboot.emp;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/emp")
public class empc {
	
	@Autowired
	private emps empservice;
	
	@RequestMapping("/hom")
	public String home() {
		return "Welcome";
	}
	
	@RequestMapping("")
	public List<emp> empdetails(){
		return empservice.getallemp();
	}
	
	@RequestMapping("/{id}")
	public emp singleempdetail(@PathVariable("id") int b) {
		return empservice.getemp(b);
	}
	
	@RequestMapping(method=RequestMethod.POST , value="")
	public void addemp(@RequestBody emp e) {
		 empservice.addemp(e);
	}
	
	@RequestMapping(method=RequestMethod.PUT ,value= "/{id}")
	public void updateemp(@PathVariable("id") int b , @RequestBody emp e) {
		empservice.updateemp(b,e);
	}
	
	@RequestMapping(value="/{id}",method=RequestMethod.DELETE)
	public void deleteemp(@PathVariable("id") int b ) {
		empservice.deleteemp(b);
	}
}
