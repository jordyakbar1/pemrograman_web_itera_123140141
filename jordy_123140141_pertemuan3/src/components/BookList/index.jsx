import React, { useState } from 'react';
import BookForm from '../BookForm';


export default function BookList({ books, onDelete, onUpdate }){
const [editingId, setEditingId] = useState(null);


return (
<div className="space-y-4">
{books.length === 0 && <div className="text-muted">Tidak ada buku</div>}
{books.map(book => (
<div key={book.id} className="p-3 bg-white rounded shadow-sm flex items-start justify-between">
<div>
<div className="font-semibold">{book.title}</div>
<div className="text-sm text-gray-600">{book.author} • <span className="capitalize">{book.status}</span></div>
</div>
<div className="flex gap-2">
<button onClick={() => setEditingId(book.id)} className="px-2 py-1 border rounded">Edit</button>
<button onClick={() => onDelete(book.id)} className="px-2 py-1 border rounded">Hapus</button>
</div>
{editingId === book.id && (
<div className="w-full mt-4">
<BookForm initial={book} onSubmit={(changes)=>{ onUpdate(book.id, changes); setEditingId(null); }} onCancel={() => setEditingId(null)} />
</div>
)}
</div>
))}
</div>
);
}