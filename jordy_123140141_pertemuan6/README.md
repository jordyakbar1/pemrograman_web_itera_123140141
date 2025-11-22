# Tugas Praktikum - Aplikasi Manajemen Matakuliah (Pyramid)

Instruksi singkat untuk menjalankan aplikasi ini.

Persyaratan
- Python 3.8+ (disarankan 3.10+)
- virtualenv

Instalasi
1. Buat virtualenv dan aktifkan:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependensi:

```powershell
pip install -r requirements.txt
```

Inisialisasi database dan seed data

```powershell
# jalankan seed untuk membuat tabel dan 3 data awal
# jalankan dari parent folder (workspace root) dengan -m untuk memastikan impor paket
python -m jordy_123140141_pertemuan6.seed_db
```

Menjalankan server

```powershell
# jalankan waitress bind ke localhost
waitress-serve --listen=127.0.0.1:6543 --call jordy_123140141_pertemuan6:main
```

Akses
- UI (simple): `http://localhost:6543/`
- API endpoints:
  - `GET /api/matakuliah` - ambil semua
  - `GET /api/matakuliah/{id}` - ambil satu
  - `POST /api/matakuliah` - tambah
  - `PUT /api/matakuliah/{id}` - update
  - `DELETE /api/matakuliah/{id}` - hapus

Tentang migrasi (Alembic)

Project ini menggunakan SQLAlchemy secara langsung. Jika ingin menambahkan migrasi dan versi DB, Anda bisa menginisialisasi Alembic secara manual:

```powershell
pip install alembic
alembic init alembic
# edit alembic.ini dan env.py untuk mengarahkan ke engine/metadata dari database.py
```

Catatan
- `seed_db.py` akan menambahkan 3 matakuliah contoh jika tabel kosong.
- Pastikan jalankan server pada `localhost`/`127.0.0.1`, jangan memakai `0.0.0.0` pada browser.

## Dokumentasi Lengkap

### Deskripsi Proyek
Aplikasi sederhana untuk manajemen data matakuliah menggunakan Pyramid + SQLAlchemy dan SQLite. Menyediakan REST API untuk melakukan operasi CRUD pada model `Matakuliah`.

### Cara Instalasi

1. Buat virtual environment dan aktifkan (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependensi:

```powershell
pip install -r requirements.txt
```

### Konfigurasi Database

Project menggunakan SQLite secara default (`matakuliah.db` di folder kerja). Anda tidak perlu konfigurasi tambahan untuk praktik ini.

Jika ingin menggunakan DB lain, edit `DATABASE_URL` di `database.py`.

### Menjalankan Migrasi (Alembic)

Project ini tidak menyertakan konfigurasi Alembic secara default. Jika Anda ingin menambahkan migrasi:

```powershell
pip install alembic
alembic init alembic
# kemudian edit alembic/env.py untuk mengimpor engine dan Base dari `database.py`
```

### Inisialisasi Database & Seed Data

Jalankan seed script untuk membuat tabel dan menambahkan 3 data awal (jalankan dari parent folder workspace):

```powershell
python -m jordy_123140141_pertemuan6.seed_db
```

### Menjalankan Server

Gunakan `waitress-serve` dan bind ke `127.0.0.1` sehingga dapat diakses di browser:

```powershell
waitress-serve --listen=127.0.0.1:6543 --call jordy_123140141_pertemuan6:main
```

API akan tersedia di `http://localhost:6543/` (UI sederhana) dan endpoint JSON di `/api/matakuliah`.

## API Endpoints

Model `Matakuliah` memiliki atribut:

- `id` (Integer, primary key, auto increment)
- `kode_mk` (Text, unique, not null)
- `nama_mk` (Text, not null)
- `sks` (Integer, not null)
- `semester` (Integer, not null)

Base URL: `http://localhost:6543`

### 1. Get All Matakuliah
**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah
```

**Response (200):**
```json
[
  {
    "id": 1,
    "kode_mk": "MK001",
    "nama_mk": "Algoritma dan Pemrograman",
    "sks": 3,
    "semester": 1
  },
  {
    "id": 2,
    "kode_mk": "MK002",
    "nama_mk": "Basis Data",
    "sks": 3,
    "semester": 2
  }
]
```

### 2. Get Matakuliah by ID
**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

**Response (200):**
```json
{
  "id": 1,
  "kode_mk": "MK001",
  "nama_mk": "Algoritma dan Pemrograman",
  "sks": 3,
  "semester": 1
}
```

**Error (404):** jika tidak ditemukan
```json
{ "error": "Matakuliah tidak ditemukan" }
```

### 3. Create Matakuliah (POST)
**Request:**
```bash
curl -X POST http://localhost:6543/api/matakuliah \
  -H 'Content-Type: application/json' \
  -d '{"kode_mk":"MK010","nama_mk":"Jaringan Komputer","sks":3,"semester":4}'
```

**Response (200):** (objek yang dibuat)
```json
{
  "id": 10,
  "kode_mk": "MK010",
  "nama_mk": "Jaringan Komputer",
  "sks": 3,
  "semester": 4
}
```

**Error (400):** jika `kode_mk` duplikat atau field wajib tidak lengkap
```json
{ "error": "kode_mk sudah ada" }
```

### 4. Update Matakuliah (PUT)
**Request:**
```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H 'Content-Type: application/json' \
  -d '{"nama_mk":"Algoritma Lanjut","sks":4}'
```

**Response (200):** (objek yang sudah diupdate)
```json
{
  "id": 1,
  "kode_mk": "MK001",
  "nama_mk": "Algoritma Lanjut",
  "sks": 4,
  "semester": 1
}
```

**Error (400):** jika ID tidak valid atau `kode_mk` duplikat ketika diganti

### 5. Delete Matakuliah (DELETE)
**Request:**
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

**Response (200):**
```json
{ "status": "deleted" }
```

## Testing

Contoh perintah `curl` untuk menguji tiap endpoint sudah disertakan di atas. Berikut rangkuman singkat:

- Inisialisasi + seed:
```bash
python -m jordy_123140141_pertemuan6.seed_db
```
- Cek semua:
```bash
curl -X GET http://localhost:6543/api/matakuliah
```
- Tambah data:
```bash
curl -X POST http://localhost:6543/api/matakuliah -H 'Content-Type: application/json' -d '{"kode_mk":"MK011","nama_mk":"Pemrograman Web","sks":3,"semester":2}'
```
- Update data:
```bash
curl -X PUT http://localhost:6543/api/matakuliah/2 -H 'Content-Type: application/json' -d '{"nama_mk":"Basis Data Lanjut"}'
```
- Hapus data:
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/2
```

## Catatan Tambahan

- Pastikan virtualenv aktif saat menjalankan perintah `pip` atau `python`.
- Jika Anda ingin menggunakan Alembic, saya dapat membantu menambahkan folder `alembic/` dan konfigurasi otomatis.

Jika mau, saya bisa juga membuat file `postman_collection.json` atau menambahkan test script otomatis untuk CI.
