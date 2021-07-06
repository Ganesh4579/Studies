package com.test.Hibernate;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.MapsId;
import javax.persistence.OneToOne;
import javax.persistence.Table;


@Entity
@Table(name="home_v3")
public class home {
	
	@Id
	private int id;
//	@Column(name="name")
//	private Name name;
	@Column(name="age")
	private double age;
 
	@Column(name="role")
	private String role;
	
	@ElementCollection
	private Set<Name> names =new HashSet<Name>();
	
	public Set<Name> getNames() {
		return names;
	}
	public void setNames(Set<Name> names) {
		this.names = names;
	}
//	@OneToOne()
//	@JoinColumn(name="school_info")
//	private school s;
//	
//	public school getS() {
//		return s;
//	}
//	public void setS(school s) {
//		this.s = s;
//	}
	public int getId() {
		return id;
	}
//	@Override
//	public String toString() {
//		return "home [id=" + id + ", name=" + name + ", age=" + age + ", role=" + role + "]";
//	}
	public void setId(int id) {
		this.id = id;
	}
@Override
	public String toString() {
		return "home [id=" + id + ", age=" + age + ", role=" + role + "]";
	}
	//
//	public Name getName() {
//		return name;
//	}
//	public void setName(Name name) {
//		this.name = name;
//	}
	public double getAge() {
		return age;
	}
	public void setAge(double d) {
		this.age = d;
	}
	public String getRole() {
		return role;
	}
	public void setRole(String role) {
		this.role = role;
	}
}
