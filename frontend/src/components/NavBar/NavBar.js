import React from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import logo from "../../assets/logo.png";
import styles from "./NavBar.module.css";
import { NavLink } from "react-router-dom";
import ColorModeToggle from "../ColorModeToggle";
import { useColorModeContext } from "../../contexts/ColorModeContext";

const NavBar = () => {
  const { isDarkMode } = useColorModeContext();

  return (
    <Navbar
      expand="md"
      fixed="top"
      data-bs-theme={isDarkMode ? "dark" : "light"}
      className={`${styles.NavBar} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}

    >
      <Container>
        <NavLink to="/">
          <Navbar.Brand>
            <img src={logo} alt="logo" height="60px"></img>
          </Navbar.Brand>
        </NavLink>
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav
            className="ms-auto text-start align-items-end"
          >
            <NavLink
              className={`${styles.NavLink} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              activeClassName={`${styles.Active} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              data-bs-theme={isDarkMode ? "dark" : "light"}
              to="/"
              exact
            >
              <i className="fas fa-home"></i>Home
            </NavLink>
            <NavLink
              className={`${styles.NavLink} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              activeClassName={`${styles.Active} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              to="/login"
            >
              <i className="fas fa-sign-in-alt"></i>Sign in
            </NavLink>
            <NavLink
              className={`${styles.NavLink} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              activeClassName={`${styles.Active} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              to="/create"
            >
              <i className="fas fa-user-plus"></i>Sign up
            </NavLink>
            <NavLink
              className={`${styles.NavLink} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              activeClassName={`${styles.Active} ${isDarkMode ? styles["dark-mode"] : styles["light-mode"]}`}
              to="/user-favorites/"
            >
              <i className="fa-solid fa-heart"></i>
              My Favorite
            </NavLink>
            <ColorModeToggle></ColorModeToggle>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;