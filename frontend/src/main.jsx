import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css"; // Import Tailwind base styles

ReactDOM.createRoot(document.getElementById("root")).render(
  // Removed StrictMode for simplicity during development
  <App />,
);
