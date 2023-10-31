import axios from "axios";

// Axios Global settings
axios.defaults.headers.post["Contnet-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

// IMPORTANT!!
// Because this React app is running in the same workspace as the API,

 // there is no need to set a separate baseURL until you reach deployment.

 // Setting a baseURL before you reach deployment will cause errors
