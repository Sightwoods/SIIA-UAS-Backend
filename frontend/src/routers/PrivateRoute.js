import React from 'react';

import { Navigate, useLocation } from "react-router-dom";

export const PrivateRoute = ({ isAuthenticated, children }) => {
    let location = useLocation();
  
    if (!isAuthenticated) {
      return <Navigate to="/login" state={{ from: location }} />;
    }
  
    return children;
}
