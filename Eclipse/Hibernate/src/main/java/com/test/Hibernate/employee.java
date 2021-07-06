package com.test.Hibernate;


import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;

@Entity
public class employee {
	@Id
	private int empid;
	private String name;
	private int salary;
	
	@OneToOne
	@JoinColumn(name="branch_id")
	private branch branch;
//	
//	@ElementCollection
//	private Set<String> set=new HashSet<String>();
//	
//	
//	public Set<String> getSet() {
//		return set;
//	}
//	public void setSet(Set<String> set) {
//		this.set = set;
//	}
	public branch getBranch() {
		return branch;
	}
	public void setBranch(branch branch) {
		this.branch = branch;
	}
	public int getEmpid() {
		return empid;
	}
	public void setEmpid(int empid) {
		this.empid = empid;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getSalary() {
		return salary;
	}
	public void setSalary(int salary) {
		this.salary = salary;
	}
	@Override
	public String toString() {
		return "employee [empid=" + empid + ", name=" + name + ", salary=" + salary + "]";
	}

	
	
}
