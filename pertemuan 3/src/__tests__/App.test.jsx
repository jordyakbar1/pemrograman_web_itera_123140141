import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { BrowserRouter } from 'react-router-dom';
import App from '../App';
import { BookProvider } from '../context/BookContext';


function renderApp(){
return render(
<BrowserRouter>
<BookProvider>
<App />
</BookProvider>
</BrowserRouter>
);
}


test('renders header and navigation', () => {
renderApp();
expect(screen.getByText(/Manajemen Buku Pribadi/i)).toBeInTheDocument();
expect(screen.getByText(/Home/i)).toBeInTheDocument();
});