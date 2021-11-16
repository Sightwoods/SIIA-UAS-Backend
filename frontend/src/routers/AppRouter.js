import { BrowserRouter, Route, Routes } from 'react-router-dom';

import { PrivateRoute } from './PrivateRoute';
import { PublicRoute } from './PublicRoute';

import { LoginScreen } from '../components/auth/LoginScreen';
import { HomeScreen } from '../components/HomeScreen';

const value = false;

export const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    element={
                        <PrivateRoute isAuthenticated={value}>
                            <HomeScreen /> 
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
