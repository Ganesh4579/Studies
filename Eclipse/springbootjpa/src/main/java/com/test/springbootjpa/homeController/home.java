package com.test.springbootjpa.homeController;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class home {
	@RequestMapping("/home")
	public String homepage() {
		return "Welcome";
	}
}
