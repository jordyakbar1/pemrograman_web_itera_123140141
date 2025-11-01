import React from 'react';
import { useBooks } from '../../context/BookContext';
import useBookStats from '../../hooks/useBookStats';


export default function Stats(){
const { books } = useBooks();
const stats = useBookStats(books);


return (
<div className="p-4 bg-white rounded shadow-sm">
<h2 className="text-xl font-semibold">Statistik Buku</h2>
<div className="mt-4">
<div>Total buku: <strong>{stats.total}</strong></div>
<div className="mt-2">Per status:</div>
<ul className="list-disc pl-6">
<li>Milik: {stats.byStatus.milik || 0}</li>
<li>Sedang dibaca: {stats.byStatus.baca || 0}</li>
<li>Ingin dibeli: {stats.byStatus.beli || 0}</li>
</ul>
</div>
</div>
);
}