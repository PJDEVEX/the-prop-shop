// Import the necessary dependencies
import { useState, useEffect } from "react";

// Create a custom hook to manage color mode
export function useColorMode() {
  // Check if the user's dark mode preference is stored in local storage
  useEffect(() => {
    const storedDarkMode = localStorage.getItem("isDarkMode");
    if (storedDarkMode) {
      // Set the initial dark mode state based on local storage
      setIsDarkMode(storedDarkMode === "true");
    }
  }, []);
  // State to track whether the app is in dark mode or not
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Toggle the color mode between light and dark
  const toggleColorMode = () => {
    setIsDarkMode((prevMode) => !prevMode);
    // Store the current color mode in local storage for persistence
    localStorage.setItem("isDarkMode", !isDarkMode);
  };

  // Return the color mode state and toggle function
  return { isDarkMode, toggleColorMode };
}
