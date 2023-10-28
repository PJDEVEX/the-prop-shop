import React from 'react';
import { useColorModeContext } from '../contexts/ColorModeContext';
import '@theme-toggles/react/css/Classic.css';
import { Classic } from '@theme-toggles/react';

const ColorModeToggle = () => {
  const { isDarkMode, toggleColorMode } = useColorModeContext();

  const handleToggleClick = () => {
    toggleColorMode();
  };

  console.log('isDarkMode:', isDarkMode);

  return (
    <Classic
      duration={750}
      toggled={isDarkMode}
      onToggle={handleToggleClick}
    />
  );
};

export default ColorModeToggle;
