import React, { useState, useEffect } from 'react';


export default function BookForm({ onSubmit, initial = null, onCancel }){
const [title, setTitle] = useState(initial?.title || '');
const [author, setAuthor] = useState(initial?.author || '');
const [status, setStatus] = useState(initial?.status || 'milik');
const [errors, setErrors] = useState({});


useEffect(() => {
setTitle(initial?.title || '');
setAuthor(initial?.author || '');
setStatus(initial?.status || 'milik');
}, [initial]);


const validate = () => {
const e = {};
if (!title.trim()) e.title = 'Judul wajib diisi';
if (!author.trim()) e.author = 'Penulis wajib diisi';
if (!['milik','baca','beli'].includes(status)) e.status = 'Status tidak valid';
setErrors(e);
return Object.keys(e).length === 0;
};


const handleSubmit = (ev) => {
ev.preventDefault();
if (!validate()) return;
try{
onSubmit({ title: title.trim(), author: author.trim(), status });
setTitle(''); setAuthor(''); setStatus('milik');
} catch (err){
console.error(err);
setErrors({ form: 'Gagal menyimpan buku' });
}
};


return (
<form onSubmit={handleSubmit} className="p-4 bg-white rounded shadow-sm space-y-3">
{errors.form && <div className="text-red-600">{errors.form}</div>}
<div>
<label className="block text-sm font-medium">Judul</label>
<input value={title} onChange={e=>setTitle(e.target.value)} className="w-full p-2 border rounded" />
{errors.title && <div className="text-xs text-red-600">{errors.title}</div>}
</div>
<div>
<label className="block text-sm font-medium">Penulis</label>
<input value={author} onChange={e=>setAuthor(e.target.value)} className="w-full p-2 border rounded" />
{errors.author && <div className="text-xs text-red-600">{errors.author}</div>}
</div>
<div>
<label className="block text-sm font-medium">Status</label>
<select value={status} onChange={e=>setStatus(e.target.value)} className="w-full p-2 border rounded">
<option value="milik">Milik</option>
<option value="baca">Sedang dibaca</option>
<option value="beli">Ingin dibeli</option>
</select>
{errors.status && <div className="text-xs text-red-600">{errors.status}</div>}
</div>
<div className="flex gap-2">
<button type="submit" className="px-4 py-2 rounded bg-blue-600 text-white">Simpan</button>
{onCancel && (<button type="button" onClick={onCancel} className="px-4 py-2 rounded border">Batal</button>)}
</div>
</form>
);
}