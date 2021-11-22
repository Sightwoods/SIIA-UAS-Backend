import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { HomeScreen } from '../pages/HomeScreen';

export const HomeRouter = () => {
    return (
        <Routes>
            {/* <Route path="/query" element={<QueryScreen />} /> */}

            <Route path="/" element={<HomeScreen />} />
        </Routes>
    )
}
