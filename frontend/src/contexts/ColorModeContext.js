import React, { createContext, useContext, useEffect } from 'react';
import { useColorMode } from '../hooks/useColorMode';

// Create a context for managing color mode
const ColorModeContext = createContext();

// Custom hook to access the color mode context
export function useColorModeContext() {
  return useContext(ColorModeContext);
}

export function ColorModeProvider({ children }) {
  const { isDarkMode, toggleColorMode } = useColorMode();

  // Apply the .dark-mode class to the body element conditionally
  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }, [isDarkMode]);

  // Provide the color mode state and toggle function to child components
  return (
    <ColorModeContext.Provider value={{ isDarkMode, toggleColorMode }}>
      {children}
    </ColorModeContext.Provider>
  );
}
