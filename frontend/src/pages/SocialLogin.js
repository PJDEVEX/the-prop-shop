import React from "react";
import { useState } from "react"; 
import SocialLoginButton from "./../components/SocialLoginButton/SocialSignInButton";
import { facebookLogin, googleLogin } from "../api/axiosDefaults";

const SocialLogin = () => {
  const [error, setError] = useState(null); 

  // Handle the response from Facebook login
  async function responseFb(response) {
    try {
      console.log(response);
      // Attempt to log in with Facebook
      await facebookLogin(response.accessToken);
    } catch (error) {
      console.error("Error in Facebook login:", error);
      setError("Failed to log in with Facebook. Please try again.");
    }
  }

  // Handle the response from Google login
  async function responseGoogle(response) {
    try {
      console.log(response);
      // Attempt to log in with Google
      await googleLogin(response.accessToken);
    } catch (error) {
      console.error("Error in Google login:", error);
      setError("Failed to log in with Google. Please try again.");
    }
  }

  return (
    <div>
      {error && <div className="error">{error}</div>}
      <SocialLoginButton provider="facebook" onClick={responseFb} />
      <SocialLoginButton provider="google" onClick={responseGoogle} />
    </div>
  );
}

export default SocialLogin;