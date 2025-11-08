def hitung_nilai_akhir(mhs):
    return 0.3 * mhs["nilai_uts"] + 0.4 * mhs["nilai_uas"] + 0.3 * mhs["nilai_tugas"]

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def tampilkan_data(data):
    print("=" * 75)
    print(f"{'Nama':<15}{'NIM':<10}{'UTS':<8}{'UAS':<8}{'Tugas':<8}{'Akhir':<10}{'Grade'}")
    print("=" * 75)
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs)
        grade = tentukan_grade(nilai_akhir)
        print(f"{mhs['nama']:<15}{mhs['nim']:<10}{mhs['nilai_uts']:<8}{mhs['nilai_uas']:<8}{mhs['nilai_tugas']:<8}{nilai_akhir:<10.2f}{grade}")
    print("=" * 75)

def cari_tertinggi(data):
    return max(data, key=lambda mhs: hitung_nilai_akhir(mhs))

def cari_terendah(data):
    return min(data, key=lambda mhs: hitung_nilai_akhir(mhs))

def filter_berdasarkan_grade(data, grade_dicari):
    hasil = []
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs)
        grade = tentukan_grade(nilai_akhir)
        if grade == grade_dicari.upper():
            hasil.append(mhs)
    return hasil

def rata_rata_kelas(data):
    total = sum(hitung_nilai_akhir(mhs) for mhs in data)
    return total / len(data)

def input_data_awal():
    data = []
    jumlah = int(input("Berapa banyak mahasiswa yang ingin dimasukkan (minimal 5)? "))
    if jumlah < 5:
        jumlah = 5
        print("Minimal 5 data, akan dimasukkan 5 mahasiswa.")

    for i in range(jumlah):
        print(f"\nData mahasiswa ke-{i+1}")
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        tugas = float(input("Masukkan nilai Tugas: "))
        data.append({
            "nama": nama,
            "nim": nim,
            "nilai_uts": uts,
            "nilai_uas": uas,
            "nilai_tugas": tugas
        })
    return data

def tambah_mahasiswa(data):
    print("\n=== Tambah Data Mahasiswa Baru ===")
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    tugas = float(input("Masukkan nilai Tugas: "))
    data.append({"nama": nama, "nim": nim, "nilai_uts": uts, "nilai_uas": uas, "nilai_tugas": tugas})
    print("Data berhasil ditambahkan!\n")


def menu():
    data_mahasiswa = input_data_awal()

    while True:
        print("\n=== PROGRAM PENGELOLAAN DATA NILAI MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Tambah Data Mahasiswa")
        print("3. Cari Nilai Tertinggi")
        print("4. Cari Nilai Terendah")
        print("5. Filter Berdasarkan Grade")
        print("6. Hitung Rata-rata Nilai Kelas")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
        elif pilihan == "2":
            tambah_mahasiswa(data_mahasiswa)
        elif pilihan == "3":
            tertinggi = cari_tertinggi(data_mahasiswa)
            print("\nMahasiswa dengan nilai tertinggi:")
            tampilkan_data([tertinggi])
        elif pilihan == "4":
            terendah = cari_terendah(data_mahasiswa)
            print("\nMahasiswa dengan nilai terendah:")
            tampilkan_data([terendah])
        elif pilihan == "5":
            g = input("Masukkan grade (A/B/C/D/E): ")
            hasil = filter_berdasarkan_grade(data_mahasiswa, g)
            if hasil:
                print(f"\nMahasiswa dengan grade {g.upper()}:")
                tampilkan_data(hasil)
            else:
                print("Tidak ada mahasiswa dengan grade tersebut.")
        elif pilihan == "6":
            print(f"\nRata-rata nilai kelas: {rata_rata_kelas(data_mahasiswa):.2f}")
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

menu()
