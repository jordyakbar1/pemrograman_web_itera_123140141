import React, { createContext, useContext } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';


const BookContext = createContext(null);


export function BookProvider({ children }){
const [books, setBooks] = useLocalStorage('books_v1', []);


// CRUD helpers
const addBook = (book) => {
setBooks(prev => [{...book, id: Date.now().toString()}, ...prev]);
};


const updateBook = (id, changes) => {
setBooks(prev => prev.map(b => b.id === id ? {...b, ...changes} : b));
};


const deleteBook = (id) => {
setBooks(prev => prev.filter(b => b.id !== id));
};


return (
<BookContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
{children}
</BookContext.Provider>
);
}


export function useBooks(){
const ctx = useContext(BookContext);
if (!ctx) throw new Error('useBooks must be used within BookProvider');
return ctx;
}