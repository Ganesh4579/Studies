package com.test.springboot.emp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;

@Service
public class emps {
	
	
	private List<emp> empd= new ArrayList<emp> ( Arrays.asList(
			new emp(1001,"Thanushree",1),
			new emp(1002,"Ganesh",22),
			new emp(1003,"Prakash",29)
			)
			);
	
	public List<emp> getempdetails(){
		return empd;
	}
	

	public emp getbyid(int a) {
		
		//return (emp) empd.stream().filter(e -> e.getId() == a);
		
		emp ew=null;
		
		for (emp e: empd) {
			if (e.getId() == a) {
				 ew =e;
			}
		}
		return ew;
	}


	public void  addemp(emp e) {
		empd.add(e);
	}


	public void updateemp(int b, emp e) {
		for (int i=0 ; i<empd.size() ; i++) {
			emp ew=empd.get(i);
			if (ew.getId()==b) {
				empd.set(i, e);
			}
		}
		
	}


	public void deleteemp(int b) {
		for (int i=0 ; i<empd.size() ; i++) {
			emp ew=empd.get(i);
			if (ew.getId()==b) {
				empd.remove(i);
			}
		}

		
	}
}
