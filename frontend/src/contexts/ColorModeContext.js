import React, { createContext, useContext, useState, useEffect } from 'react';

// Create a context for managing color mode.
const ColorModeContext = createContext();

// Custom hook to access the color mode context.
export function useColorMode() {
  return useContext(ColorModeContext);
}

export function ColorModeProvider({ children }) {
  // Check if the user's dark mode preference is stored in local storage.
  useEffect(() => {
    const storedDarkMode = localStorage.getItem('isDarkMode');
    if (storedDarkMode) {
      // Set the initial dark mode state based on local storage.
      setIsDarkMode(storedDarkMode === 'true');
    }
  }, []);

  // State to track whether the app is in dark mode or not.
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Toggle the color mode between light and dark.
  const toggleColorMode = () => {
    setIsDarkMode((prevMode) => !prevMode);
    // Store the current color mode in local storage for persistence.
    localStorage.setItem('isDarkMode', !isDarkMode);
  };

  // Apply the .dark-mode class to the body element conditionally.
  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }, [isDarkMode]);

  // Provide the color mode state and toggle function to child components.
  return (
    <ColorModeContext.Provider value={{ isDarkMode, toggleColorMode }}>
      {children}
    </ColorModeContext.Provider>
  );
}
