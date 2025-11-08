import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Stats from './pages/Stats';


export default function App(){
return (
<div className="min-h-screen p-6 font-sans bg-gray-50">
<header className="mb-6">
<nav className="flex items-center justify-between">
<h1 className="text-2xl font-bold">Manajemen Buku Pribadi</h1>
<div className="space-x-4">
<Link to="/" className="underline">Home</Link>
<Link to="/stats" className="underline">Stats</Link>
</div>
</nav>
</header>
<main>
<Routes>
<Route path="/" element={<Home/>} />
<Route path="/stats" element={<Stats/>} />
</Routes>
</main>
</div>
);
}