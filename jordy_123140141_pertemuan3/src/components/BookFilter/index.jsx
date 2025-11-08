import React, { useState } from 'react';


export default function BookFilter({ onFilter }){
const [query, setQuery] = useState('');
const [status, setStatus] = useState('all');


const apply = () => onFilter({ query, status });


return (
<div className="p-3 bg-white rounded shadow-sm flex gap-3 items-end">
<div className="flex-1">
<label className="block text-sm">Cari</label>
<input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Judul atau penulis" className="w-full p-2 border rounded" />
</div>
<div>
<label className="block text-sm">Status</label>
<select value={status} onChange={e=>setStatus(e.target.value)} className="p-2 border rounded">
<option value="all">Semua</option>
<option value="milik">Milik</option>
<option value="baca">Sedang dibaca</option>
<option value="beli">Ingin dibeli</option>
</select>
</div>
<div>
<button onClick={apply} className="px-4 py-2 rounded bg-green-600 text-white">Terapkan</button>
</div>
</div>
);
}