// webapp/frontend/src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';  // Use the correct import for React 18
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));  // Create a root with createRoot
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
