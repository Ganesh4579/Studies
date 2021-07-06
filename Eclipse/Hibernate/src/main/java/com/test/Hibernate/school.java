package com.test.Hibernate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;

@Entity
public class school {
	
	@Id
	private int rollnum;
	@Column(name="mark")
	private float mark;
	@Column(name="roles")
	private String roles;

	public int getRollnum() {
		return rollnum;
	}
	public void setRollnum(int rollnum) {
		this.rollnum = rollnum;
	}
	public float getMark() {
		return mark;
	}
	public void setMark(float mark) {
		this.mark = mark;
	}
	public String getRole() {
		return roles;
	}
	public void setRole(String role) {
		this.roles = role;
	}
	
}
