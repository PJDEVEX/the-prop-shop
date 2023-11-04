import axios from "axios";

// Axios Global settings
axios.defaults.headers.post["Contnet-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

// IMPORTANT!!
// Because this React app is running in the same workspace as the API,

// there is no need to set a separate baseURL until you reach deployment.

// Setting a baseURL before you reach deployment will cause errors

// Create an Axios instance for your specific needs

// Import environment variables for social login
const facebookClientId = process.env.SOCIAL_AUTH_FACEBOOK_KEY;
const facebookClientSecret = process.env.SOCIAL_AUTH_FACEBOOK_SECRET;
const googleClientId = process.env.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY;
const googleClientSecret = process.env.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET;

export async function facebookLogin(accessToken) {
  try {
    const response = await axios.post(`/api-auth/convert-token`, {
      token: accessToken,
      backend: "facebook",
      grant_type: "convert_token",
      client_id: facebookClientId,
      client_secret: facebookClientSecret,
    });
    // Save the access and refresh tokens
    console.log(response.data);
    return response.data; // Return the response data if needed
  } catch (error) {
    // Handle and log errors
    console.error("Error in facebookLogin:", error);
    throw error; // Re-throw the error for further handling
  }
}
export async function googleLogin(accessToken) {
  try {
    const response = await axios.post(`/api-auth/convert-token`, {
      token: accessToken,
      backend: "google-oauth2",
      grant_type: "convert_token",
      client_id: googleClientId,
      client_secret: googleClientSecret,
    });
    // Save the access and refresh tokens
    console.log(response.data);
    return response.data; // Return the response data if needed
  } catch (error) {
    // Handle and log errors
    console.error("Error in googleLogin:", error);
    throw error; // Re-throw the error for further handling
  }
}
const axiosInstance = axios.create({
  baseURL: "https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/",
});

// Add the interceptor to handle token expiration and refresh
axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error;
    console.log(originalRequest);

    if (typeof error.response === "undefined") {
      alert("A server error happened. We will fix it shortly.");
      return Promise.reject(error);
    }

    if (
      error.response.status === 401 &&
      !localStorage.getItem("refresh_token")
    ) {
      window.location.href = "/login/";
      return Promise.reject(error);
    }

    if (
      error.response.status === 401 &&
      error.response.statusText === "Unauthorized" &&
      localStorage.getItem("refresh_token") !== undefined
    ) {
      const refreshToken = localStorage.getItem("refresh_token");

      return axios
        .post("/api-auth/token", {
          client_id: googleClientId,
          client_secret: googleClientSecret,
          grant_type: "refresh_token",
          refresh_token: refreshToken,
        })
        .then((response) => {
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          window.location.reload();
          axiosInstance.defaults.headers["Authorization"] =
            "Bearer " + response.data.access_token;
        })
        .catch((err) => console.log(err));
    }
  }
);

export default axiosInstance;
