import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import logo from "../../assets/logo.png";
import styles from "./SignInUp.module.css";
import { Form, Button, Container, Alert } from "react-bootstrap";
import { useColorScheme } from "../../hooks/useColorScheme";
import axios from "axios";
import SocialLogin from "../SocialLogin";
import {useSetCurrentUser} from '../../contexts/CurrentUserContext'

function SignInForm () {
  const setCurrentUser = useSetCurrentUser();

  // Determine if the app is in dark mode
  const { isDark } = useColorScheme();
  const darkClass = isDark ? styles["dark"] : "";

  // State to store user sign-up data and errors
  const [signInData, setSignInData] = useState({
    email: "",
    password: "",
  });

  const {email, password} = signInData;

  const [errors, setErrors] = useState({});

  const history = useHistory();

  // Handle changes in form fields
  const handleChange = (event) => {
    setSignInData({
      ...signInData,
      [event.target.name]: event.target.value,
    });
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Send a POST request to create a user
      const {data } = await axios.post("api-auth/token", signInData);
      // Redirect to the sign-in page on successful registration
      setCurrentUser(data.user)
      history.push("/");
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
        Sign In
      </div>

      {/* Social Sign-In */}
      <SocialLogin />

      <Form onSubmit={handleSubmit} className={`p-3 mt-3 ${darkClass}`}>

        {/* Email Field */}
        <Form.Group
          className={`form-field d-flex align-items-center ${styles["form-field"]} ${darkClass}`}
          controlId="email"
        >
          <Form.Label className="d-none">Username</Form.Label>
          <i className="far fa-envelope"></i>
          <Form.Control
            type="email"
            name="email"
            placeholder="Enter your email"
            value={email}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.email?.map((message, idx) => (
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
            value={password}
            onChange={handleChange}
          />
        </Form.Group>
        {errors.password?.map((message, idx) => (
          <Alert variant="warning" key={idx}>
            {message}
          </Alert>
        ))}

        <Button className={`btn mt-3 ${styles.btn} ${darkClass}`} type="submit">
          Sign In
        </Button>
      </Form>

      <Container className={`mt-3 ${darkClass}`}>
        <Link className={`${styles.link} ${darkClass}`} to="/create/">
          Dont have an account? <span>Sign up now!</span>
        </Link>
      </Container>
    </div>
  );
};

export default SignInForm;
