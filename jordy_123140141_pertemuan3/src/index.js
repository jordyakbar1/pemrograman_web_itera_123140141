import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import { BookProvider } from './context/BookContext';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const root = createRoot(document.getElementById('root'));
root.render(
<React.StrictMode>
<BrowserRouter>
<BookProvider>
<App />
</BookProvider>
</BrowserRouter>
</React.StrictMode>
);