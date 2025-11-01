import React from 'react';
import { render, screen, fireEvent, within } from '@testing-library/react';
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


test('add a book and it appears in list', () => {
setup();
const title = screen.getByLabelText(/Judul/i);
const author = screen.getByLabelText(/Penulis/i);
const submit = screen.getByText(/Simpan/i);
fireEvent.change(title, { target: { value: 'Clean Code' } });
fireEvent.change(author, { target: { value: 'Robert C. Martin' } });
fireEvent.click(submit);
expect(screen.getByText(/Clean Code/i)).toBeInTheDocument();
});


test('edit a book', () => {
setup();
const title = screen.getByLabelText(/Judul/i);
const author = screen.getByLabelText(/Penulis/i);
const submit = screen.getByText(/Simpan/i);
fireEvent.change(title, { target: { value: '1984' } });
fireEvent.change(author, { target: { value: 'Orwell' } });
fireEvent.click(submit);


const editBtn = screen.getAllByText(/Edit/i)[0];
fireEvent.click(editBtn);
const editTitle = screen.getByDisplayValue('1984');
fireEvent.change(editTitle, { target: { value: 'Nineteen Eighty-Four' } });
fireEvent.click(screen.getAllByText(/Simpan/i)[1]);
expect(screen.getByText(/Nineteen Eighty-Four/i)).toBeInTheDocument();
});


test('delete a book', () => {
setup();
const title = screen.getByLabelText(/Judul/i);
const author = screen.getByLabelText(/Penulis/i);
const submit = screen.getByText(/Simpan/i);
fireEvent.change(title, { target: { value: 'ToDelete' } });
fireEvent.change(author, { target: { value: 'Author' } });
fireEvent.click(submit);


const del = screen.getAllByText(/Hapus/i)[0];
fireEvent.click(del);
expect(screen.queryByText(/ToDelete/i)).not.toBeInTheDocument();
});