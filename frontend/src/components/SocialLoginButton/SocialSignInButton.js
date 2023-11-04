import React from "react";
import { Button } from "react-bootstrap";
import styles from "./SocialSignInButton.module.css";
import facebookLogo from "../../assets/facebookLogo.png";
import googleLogo from "../../assets/googleLogo.png";

const SocialLoginButton = ({ provider, onClick }) => {
  const buttonClassName = `btn ${styles[`btn-${provider}`]}`;
  const buttonText = provider === "facebook" ? "Facebook" : "Google";
  const imageSrc = provider === "facebook" ? facebookLogo : googleLogo;

  return (
    <Button className={`mx-auto ${buttonClassName}`} onClick={onClick}>
      <img
        src={imageSrc}
        alt={`Login with ${buttonText}`}
        className={styles.logo}
      />
      {`Login with ${buttonText}`}
    </Button>
  );
};

export default SocialLoginButton;
