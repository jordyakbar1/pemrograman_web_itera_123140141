import React, { useMemo, useState } from 'react';
import { useBooks } from '../../context/BookContext';
import BookForm from '../../components/BookForm';
import BookList from '../../components/BookList';
import BookFilter from '../../components/BookFilter';


export default function Home(){
const { books, addBook, updateBook, deleteBook } = useBooks();
const [filter, setFilter] = useState({ query: '', status: 'all' });


const filtered = useMemo(() => {
const q = filter.query.trim().toLowerCase();
return books.filter(b => {
if (filter.status !== 'all' && b.status !== filter.status) return false;
if (!q) return true;
return b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q);
});
}, [books, filter]);


return (
<div className="grid grid-cols-1 gap-6">
<div className="grid lg:grid-cols-2 gap-6">
<BookForm onSubmit={(b)=>addBook(b)} />
<div>
<BookFilter onFilter={setFilter} />
<div className="mt-4">
<BookList books={filtered} onDelete={deleteBook} onUpdate={updateBook} />
</div>
</div>
</div>
</div>
);
}