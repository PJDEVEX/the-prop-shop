import React from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/logo.png";
import styles from "./SignInUp.module.css";
import { Form, Button, Container } from "react-bootstrap";
// import btnStyles from "../../styles/Button.module.css";
// import appStyles from "../../App.module.css";

const SignUpForm = () => {
  return (
    <div className={styles.wrapper}>
      <div className="logo">
        <img className={styles.logo} src={logo} alt="The Prop Shop Logo" />
      </div>
      <div class="text-center mt-4 name">The Prop Shop</div>
      <Form className="p-3 mt-3">
        {/* Username */}
        <Form.Group
          className="form-field d-flex align-items-center"
          controlId="username"
        >
          <Form.Label className="d-none">username</Form.Label>
          <i className="far fa-user"></i>

          <Form.Control type="text" name="userName" placeholder="Username" />
        </Form.Group>

        {/* Password */}
        <Form.Group
          className="form-field d-flex align-items-center"
          controlId="password1"
        >
          <Form.Label className="d-none">Password</Form.Label>
          <i className="fa-solid fa-key"></i>

          <Form.Control type="text" name="password" placeholder="Password" />
        </Form.Group>

        {/* Confirm Password */}
        <Form.Group
          className="form-field d-flex align-items-center"
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
        <Button className="btn mt-3" type="submit">
          Sign up
        </Button>
      </Form>
      <Container className="mt-3">
        <Link className={styles.Link} to="/signin">
          Already have an account? <span>Sign in</span>
        </Link>
      </Container>
    </div>
  );
};

export default SignUpForm;
