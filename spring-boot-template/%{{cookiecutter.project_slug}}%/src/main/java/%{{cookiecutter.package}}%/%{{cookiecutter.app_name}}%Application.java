package %{{cookiecutter.package}}%;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class %{{cookiecutter.app_name}}%Application {

	public static void main(String[] args) {
		SpringApplication.run(%{{cookiecutter.app_name}}%Application.class, args);
	}

}
