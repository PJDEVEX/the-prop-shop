import React from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import logo_white_bg from "../assets/logo_white_bg.png";
import styles from "../styles/NavBar.module.css";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <Navbar className={styles.NavBar} expand="md" fixed="top">
      <Container>
        {/* NavLink to the Home page when click logo */}
        <NavLink to="/">
          <Navbar.Brand>
            <img src={logo_white_bg} alt="the prop shop logo" height="60px" />
          </Navbar.Brand>
        </NavLink>

        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-left">
            {/* Home NavLink */}
            <NavLink
              className={styles.NavLink}
              activeClassName={styles.Active}
              to="/"
            >
              <i className="fas fa-home"></i>Home
            </NavLink>

            <NavLink
              className={styles.NavLink}
              activeClassName={styles.Active}
              to="/login"
            >
              <i className="fas fa-sign-in-alt"></i>Sign in
            </NavLink>

            <NavLink
            className={styles.NavLink}
            activeClassName={styles.Active}
            to="/create">
              <i className="fas fa-user-plus"></i>Sign up
            </NavLink>
            <NavLink
            className={styles.NavLink}
            activeClassName={styles.Active}
            to="/user-favorites/">
              <i className="fa-solid fa-heart"></i>My Favorites
            </NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
