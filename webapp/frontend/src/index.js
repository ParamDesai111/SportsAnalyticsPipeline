import React from 'react';
import ReactDOM from 'react-dom/client';  // Correct import for React 18
import './index.css';  // Global styles
import App from './App';  // Main app component

// Simple Error Boundary component to catch and display errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows the fallback UI
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // You can log the error to an error reporting service
    console.error("Error caught by Error Boundary:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Fallback UI when error occurs
      return (
        <div style={{ color: 'red', padding: '20px', textAlign: 'center' }}>
          <h1>Something went wrong.</h1>
          <p>{this.state.error?.toString()}</p>
        </div>
      );
    }

    return this.props.children; 
  }
}

// Create a root element with createRoot for React 18
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the app inside the root, wrapped in an error boundary
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
