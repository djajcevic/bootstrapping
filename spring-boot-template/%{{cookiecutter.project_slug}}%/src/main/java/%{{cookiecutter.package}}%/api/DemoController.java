package %{{cookiecutter.package}}%.api;

import %{{cookiecutter.package}}%.annotation.SuppressFBWarnings;
import %{{cookiecutter.package}}%.dbo.User;
import %{{cookiecutter.package}}%.repo.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.ResultSetExtractor;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@RestController
@SuppressFBWarnings("SPRING_ENDPOINT")
public class DemoController {

    private final UserRepo userRepo;

    public DemoController(UserRepo userRepo) {
        this.userRepo = userRepo;
    }

    @GetMapping("/users")
    public List<User> test() {
        return userRepo.findAll();
    }

}
