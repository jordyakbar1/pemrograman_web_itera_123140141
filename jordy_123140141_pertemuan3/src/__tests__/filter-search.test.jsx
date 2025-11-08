import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { BrowserRouter } from 'react-router-dom';
import { BookProvider } from '../context/BookContext';
import Home from '../pages/Home';


function setup(){
return render(
<BrowserRouter>
<BookProvider>
<Home />
</BookProvider>
</BrowserRouter>
);
}


test('filter by status and search', () => {
setup();
// Add two books with different statuses
const title = screen.getByLabelText(/Judul/i);
const author = screen.getByLabelText(/Penulis/i);
const submit = screen.getByText(/Simpan/i);


fireEvent.change(title, { target: { value: 'A Book' } });
fireEvent.change(author, { target: { value: 'A Author' } });
fireEvent.change(screen.getByLabelText(/Status/), { target: { value: 'milik' } });
fireEvent.click(submit);


fireEvent.change(title, { target: { value: 'B Book' } });
fireEvent.change(author, { target: { value: 'B Author' } });
fireEvent.change(screen.getByLabelText(/Status/), { target: { value: 'baca' } });
fireEvent.click(submit);


// search
fireEvent.change(screen.getByPlaceholderText(/Judul atau penulis/i), { target: { value: 'B Book' } });
fireEvent.click(screen.getByText(/Terapkan/i));
expect(screen.getByText(/B Book/i)).toBeInTheDocument();
expect(screen.queryByText(/A Book/i)).not.toBeInTheDocument();
});