import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import logo from "../../assets/logo.png";
import styles from "./SignInUp.module.css";
import { Form, Button, Container, Alert } from "react-bootstrap";
import { useColorScheme } from "../../hooks/useColorScheme";
import axios from "axios";
import SocialLogin from "../SocialLogin";

function SignUpForm () {
  // Determine if the app is in dark mode
  const { isDark } = useColorScheme();
  const darkClass = isDark ? styles["dark"] : "";

  // State to store user sign-up data and errors
  const [signUpData, setSignUpData] = useState({
    email: "",
    username: "",
    first_name: "",
    password: "",
  });

  const { email, username, first_name, password} = signUpData

  const [errors, setErrors] = useState({});

  const history = useHistory();

  // Handle changes in form fields
  const handleChange = (event) => {
    setSignUpData({
      ...signUpData,
      [event.target.name]: event.target.value,
    });
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Send a POST request to create a user
      await axios.post("/api/create/", signUpData);
      // Redirect to the sign-in page on successful registration
      history.push("/login/");
    } catch (error) {
      // Set errors if there is a response from the server
      setErrors(error.response?.data || {});
      // Log the error to the console for debugging
      console.error("Error in form submission:", error);
    }
  };

  return (
    <div className={`${styles.wrapper} ${darkClass}`}>
      <div className={styles.logo}>
        <img
          className={`${styles.logoImg} ${darkClass}`}
          src={logo}
          alt="The Prop Shop Logo"
        />
      </div>
      <div className={`text-center mt-4 ${styles.name} ${darkClass}`}>
        Sign Up
      </div>

      {/* Social Sign-In */}
      <SocialLogin />

      <Form onSubmit={handleSubmit} className={`p-3 mt-3 ${darkClass}`}>

        {/* Email Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="email"
        >
          <Form.Label className="d-none">Email</Form.Label>
          <i className="far fa-envelope"></i>
          <Form.Control
            type="email"
            name="email"
            placeholder="Email"
            value={signUpData.email}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.email?.map((message, idx) => (
          <Alert variant="warning" key={idx}>
            {message}
          </Alert>
        ))}

        {/* User Name Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="username"
        >
          <Form.Label className="d-none">User Name</Form.Label>
          <i className="far fa-user"></i>
          <Form.Control
            type="text"
            name="username"
            placeholder="User Name"
            value={signUpData.username}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.username?.map((message, idx) => (
          <Alert variant="warning" key={idx}>
            {message}
          </Alert>
        ))}

        {/* First Name Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="firstName"
        >
          <Form.Label className="d-none">First Name</Form.Label>
          <i className="far fa-user"></i>
          <Form.Control
            type="text"
            name="first_name"
            placeholder="First Name"
            value={signUpData.first_name}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.first_name?.map((message, idx) => (
          <Alert variant="warning" key={idx}>
            {message}
          </Alert>
        ))}

        {/* Password Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="password"
        >
          <Form.Label className="d-none">Password</Form.Label>
          <i className="fa-solid fa-key"></i>
          <Form.Control
            type="password"
            name="password"
            placeholder="Password"
            value={signUpData.password}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.password?.map((message, idx) => (
          <Alert variant="warning" key={idx}>
            {message}
          </Alert>
        ))}

        <Button className={`btn mt-3 ${styles.btn} ${darkClass}`} type="submit">
          Sign up
        </Button>
      </Form>

      <Container className={`mt-3 ${darkClass}`}>
        <Link className={`${styles.link} ${darkClass}`} to="/login">
          Already have an account? <span>Sign in</span>
        </Link>
      </Container>
    </div>
  );
};

export default SignUpForm;
