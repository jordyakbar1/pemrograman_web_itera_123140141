# 📚 Aplikasi Manajemen Buku Pribadi

Aplikasi ini digunakan untuk mencatat dan mengelola daftar buku pribadi — termasuk buku yang dimiliki, sedang dibaca, maupun yang ingin dibeli.  
Dibangun menggunakan **React JS** dengan pendekatan **Functional Components**, **Hooks**, dan **Context API**.

---

## 🚀 Fitur Utama

- ✏️ **Tambah Buku Baru** — input judul, penulis, dan status (Dimiliki / Sedang Dibaca / Ingin Dibeli)
- 🧩 **Edit & Hapus Buku** — memperbarui atau menghapus data buku
- 🔍 **Pencarian Buku** — mencari buku berdasarkan judul atau penulis
- 🎚️ **Filter Buku** — menampilkan buku berdasarkan status
- 💾 **Penyimpanan Otomatis** — data tersimpan di `localStorage`, tidak hilang saat halaman di-refresh
- 📊 **Halaman Statistik (Stats)** — menampilkan total buku berdasarkan status (dimiliki, dibaca, beli)

---

## ⚙️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|------------|------------|
| React JS | Library utama untuk membangun antarmuka pengguna |
| React Router DOM | Navigasi antar halaman (Home & Stats) |
| Context API | Manajemen state global antar komponen |
| Hooks (`useState`, `useEffect`) | Mengelola state dan efek samping |
| Custom Hooks (`useLocalStorage`, `useBookStats`) | Abstraksi logika penyimpanan dan statistik |
| localStorage | Penyimpanan data secara lokal di browser |
| Bootstrap | Styling dan layout yang responsif |
| React Testing Library | Pengujian komponen dan fungsionalitas aplikasi |

---


---

## 🧩 Cara Instalasi & Menjalankan Aplikasi

1. **Clone atau download repository ini**
git clone 

npm install

npm start

🖼️ Screenshot Antarmuka
Antarmuka hanya menggunakan bootstrap

![alt text](<Screenshot 2025-11-01 170341.png>)

![alt text](<Screenshot 2025-11-01 170652.png>)

⚛️ Fitur React yang Digunakan

useState — mengelola data daftar buku dan input form

useEffect — menyimpan data otomatis ke localStorage setiap perubahan

Context API — menyediakan data buku secara global ke seluruh komponen

Custom Hooks — mengabstraksi logika penyimpanan dan statistik

React Router — navigasi antar halaman (Home dan Statistik)

Bootstrap — memberikan gaya UI yang cepat dan responsif

👨‍💻 Pengembang

Nama: Jordy Anugrah Akbar
NIM: 123140141
Mata Kuliah:Praktikum Pemrograman Aplikasi Web