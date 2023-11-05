import React from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import logo from "../../assets/logo.png";
import styles from "./NavBar.module.css";
import { NavLink } from "react-router-dom";
import ColorModeToggle from "../DarkModeToggle";
import { useColorScheme } from "../../hooks/useColorScheme";
import { useCurrentUser } from "../../contexts/CurrentUserContext";

const NavBar = () => {
  const { isDark } = useColorScheme();

  // Apply the 'dark' class to the Navbar component conditionally
  const navBarClasses = `${styles.NavBar} ${isDark ? styles["dark"] : styles}`;
  console.log("Dark-navBarClasses:", isDark);

  // Apply the 'dark' class to the NavLink component conditionally
  const navLinkClasses = `${styles.NavLink} ${
    isDark ? styles["dark"] : styles
  }`;
  console.log("Dark-navLinkClasses:", isDark);

  // Apply the 'dark' class to the NavLink Active component conditionally
  const navLinkActiveClasses = `${styles.Active} ${
    isDark ? styles["dark"] : styles
  }`;
  console.log("Dark-navLinkActiveClasses:", isDark);

  const currentUser = useCurrentUser();

  const loggedInIcons = <>{currentUser?.username}</>;
  const loggedOutIcons = (
    <>
      <NavLink
        className={navLinkClasses}
        activeClassName={navLinkActiveClasses}
        to="/login"
      >
        <i className="fas fa-sign-in-alt"></i>Sign in
      </NavLink>
      <NavLink
        className={navLinkClasses}
        activeClassName={navLinkActiveClasses}
        to="/create"
      >
        <i className="fas fa-user-plus"></i>Sign up
      </NavLink>
    </>
  );

  return (
    <Navbar
      expand="md"
      sticky="top"
      data-bs-theme="dark"
      className={navBarClasses}
    >
      <Container>
        <NavLink to="/">
          <Navbar.Brand>
            <img src={logo} alt="logo" height="60px"></img>
          </Navbar.Brand>
        </NavLink>

        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto text-start align-items-end">
            <NavLink
              className={navLinkClasses}
              activeClassName={navLinkActiveClasses}
              data-bs-theme="dark"
              to="/"
              exact
            >
              <i className="fas fa-home"></i>Home
            </NavLink>
            {currentUser ? loggedInIcons : loggedOutIcons}
            <NavLink
              className={navLinkClasses}
              activeClassName={navLinkActiveClasses}
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
