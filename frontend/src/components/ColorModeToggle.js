import React from 'react';
import { useColorModeContext } from '../contexts/ColorModeContext';
import '@theme-toggles/react/css/Classic.css';
import { Classic } from '@theme-toggles/react';

const ColorModeToggle = () => {
  // Access the color mode context to get the current mode and the toggle function
  const { isDarkMode, toggleColorMode } = useColorModeContext();

  // Handle the toggle button click
  const handleToggleClick = () => {
    toggleColorMode();
  };
  // Bug print
  console.log('isDarkMode:', isDarkMode);

  return (
    // Classic toggle component
    <Classic
      duration={750}
      toggled={isDarkMode}
      onToggle={handleToggleClick}
      className='btn btn-lg'
      data-bs-theme="dark"
    />
  );
};

export default ColorModeToggle;
