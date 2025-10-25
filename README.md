Aplikasi web ini membantu mahasiswa dalam mengelola aktivitas akademik seperti mencatat, menyelesaikan, dan memantau deadline tugas.  
Aplikasi dibuat dengan **HTML, CSS, dan JavaScript murni**, serta menggunakan **localStorage** agar data tersimpan secara permanen di browser pengguna.
fitur aplikasi
✅ Menambahkan tugas baru (nama tugas, mata kuliah, dan deadline)  
✅ Mengedit informasi tugas yang sudah ada  
✅ Menandai tugas sebagai **selesai/belum selesai**  
✅ Menghapus tugas yang tidak diperlukan  
✅ Filter berdasarkan status (Semua / Selesai / Belum Selesai)  
✅ Pencarian tugas berdasarkan nama atau mata kuliah  
✅ Menampilkan jumlah tugas yang belum selesai  
✅ Menyimpan semua data ke **localStorage** (tidak hilang setelah browser ditutup)  
✅ Validasi form (nama tugas, mata kuliah, dan deadline harus diisi)

tampilan tugas yang selesai dan belum selesai
<img width="525" height="651" alt="image" src="https://github.com/user-attachments/assets/8a65fb64-d623-4846-91e8-c69e8b75b7d5" />

pencarian tugas berdasarkan kategori
<img width="409" height="230" alt="image" src="https://github.com/user-attachments/assets/d5dce267-fd1c-434d-9898-25056b504866" />

pencarian tugas berdasarkan nama
<img width="464" height="230" alt="image" src="https://github.com/user-attachments/assets/a622919d-304d-4851-8d97-b208b7843ec6" />


cara menggunakan aplikasi
Buka file index.html menggunakan browser (cukup klik 2x atau drag ke browser).
Aplikasi langsung bisa dijalankan tanpa server tambahan.

Penjelasan Teknis
Penggunaan localStorage
Semua data tugas (nama, mata kuliah, deadline, status) disimpan di browser menggunakan:
localStorage.setItem('tasks', JSON.stringify(tasks));


Saat halaman dimuat, data akan dibaca kembali:
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

Dengan begitu, data tetap tersimpan meskipun browser ditutup atau di-refresh.

Validasi Form

Sebelum tugas ditambahkan, dilakukan validasi sederhana:

if (!name || !course || !deadline) {
  alert('Semua field harus diisi!');
  return;
}
if (new Date(deadline) < new Date()) {
  alert('Deadline harus tanggal yang akan datang!');
  return;
}

Field tidak boleh kosong
Deadline harus tanggal yang valid dan belum lewat
