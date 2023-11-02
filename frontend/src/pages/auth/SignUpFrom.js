import React from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/logo.png";
import styles from "./SignInUp.module.css";
import { Form, Button, Container } from "react-bootstrap";
import { useColorScheme } from "../../hooks/useColorScheme";

const SignUpForm = () => {
  // Get the dark mode flag using the useColorScheme hook
  const { isDark } = useColorScheme();

  // Determine the 'dark' class based on the dark mode flag
  const darkClass = isDark ? styles["dark"] : "";

  return (
    <div className={`${styles.wrapper} ${darkClass}`}>
      {/* Logo Section */}
      <div className={styles.logo}>
        <img
          className={`${styles.logoImg} ${darkClass}`}
          src={logo}
          alt="The Prop Shop Logo"
        />
      </div>

      {/* Sign Up Title */}
      <div className={`text-center mt-4 ${styles.name} ${darkClass}`}>
        Sign Up
      </div>

      {/* Sign Up Form */}
      <Form className={`p-3 mt-3 ${darkClass}`}>
        {/* Username Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="username"
        >
          <Form.Label className="d-none">Username</Form.Label>
          <i className="far fa-user"></i>
          <Form.Control type="text" name="userName" placeholder="Username" />
        </Form.Group>

        {/* Password Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="password1"
        >
          <Form.Label className="d-none">Password</Form.Label>
          <i className="fa-solid fa-key"></i>
          <Form.Control type="text" name="password" placeholder="Password" />
        </Form.Group>

        {/* Confirm Password Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="password2"
        >
          <Form.Label className="d-none">Confirm Password</Form.Label>
          <i className="fa-solid fa-key"></i>
          <Form.Control
            type="text"
            name="password2"
            placeholder="Confirm Password"
          />
        </Form.Group>

        {/* Sign Up Button */}
        <Button className={`btn mt-3 ${styles.btn} ${darkClass}`} type="submit">
          Sign up
        </Button>
      </Form>

      {/* Link to Sign In */}
      <Container className={`mt-3 ${darkClass}`}>
        <Link className={`${styles.link} ${darkClass}`} to="/signin">
          Already have an account? <span>Sign in</span>
        </Link>
      </Container>
    </div>
  );
};

export default SignUpForm;
