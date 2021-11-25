import { BrowserRouter, Route, Routes } from 'react-router-dom';

import { PrivateRoute } from './PrivateRoute';
import { PublicRoute } from './PublicRoute';

import { LoginScreen } from '../pages/LoginScreen';
import { HomeRouter } from './HomeRouter';

const value = true;

export const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    element={
                        <PrivateRoute isAuthenticated={value}>
                            <HomeRouter />
                        </PrivateRoute>
                    }
                />
                <Route 
                    path="/login"
                    element={
                        <PublicRoute isAuthenticated={value}>
                            <LoginScreen />
                        </PublicRoute>
                    }
                />
            </Routes>
        </BrowserRouter>
    )
}
