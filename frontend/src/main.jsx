import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from './App';
import Coach from './Coach';
import NewCourse from './NewCourse';


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/coach" element={<Coach />} />
        <Route path="/new-course" element={<NewCourse />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
