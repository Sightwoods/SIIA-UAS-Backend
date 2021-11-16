import React from 'react';

import { Navigate, useLocation } from "react-router-dom";

export const PublicRoute = ({ isAuthenticated, children }) => {
    let location = useLocation();
  
    if (isAuthenticated) {
      return <Navigate to="/" state={{ from: location }} />;
    }
  
    return children;
}