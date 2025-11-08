import { useMemo } from 'react';


export default function useBookStats(books){
return useMemo(() => {
const total = books.length;
const byStatus = books.reduce((acc, b) => {
acc[b.status] = (acc[b.status] || 0) + 1;
return acc;
}, {});
return { total, byStatus };
}, [books]);
}