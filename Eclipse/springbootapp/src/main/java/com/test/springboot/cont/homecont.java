package com.test.springboot.cont;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class homecont {

	
		@RequestMapping("/home")
		public String home() {
			return "Welcome";
		}
}
