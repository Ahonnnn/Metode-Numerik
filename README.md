Optimasi Titik Impas UMKM dengan Metode Newton-Raphson
Repositori ini berisi implementasi program komputasi pencarian akar (root finding) menggunakan Python. Proyek ini disusun sebagai pemenuhan Tugas Portofolio Akhir Semester untuk mata kuliah Metode Numerik.

Program ini mendemonstrasikan perbandingan antara kecepatan komputasi mesin dengan perhitungan manual iteratif, sekaligus melakukan analisis galat (error) hampiran.

Deskripsi Kasus
Studi kasus yang diangkat adalah penentuan Titik Impas (Break-Even Point) untuk volume produksi UMKM. Karena adanya faktor biaya operasional yang dinamis dan potongan harga khusus, fungsi keuntungan bersih yang didapat tidak berjalan linier.

Oleh karena itu, permasalahan diubah menjadi pencarian akar persamaan matematis. Titik impas tercapai ketika fungsi keuntungan f(x) bernilai tepat nol.

Pemodelan Matematika
Fungsi keuntungan UMKM dimodelkan sebagai persamaan polinomial derajat tiga:
f(x) = -0.5x^3 + 4x^2 - 2x - 5

Laju perubahan keuntungan (Turunan Pertama):
f'(x) = -1.5x^2 + 8x - 2

Metode Penyelesaian: Newton-Raphson
Rumus Iterasi:
x_(n+1) = x_n - ( f(x_n) / f'(x_n) )

Fitur Program:
- Perhitungan Iteratif Otomatis: Menghitung nilai hampiran x secara berulang berdasarkan tebakan awal.
- Tabel Output Rapi: Menampilkan hasil setiap langkah (Iterasi, Nilai x, Nilai f(x), dan Galat) langsung di command line interface (CLI).
- Validasi Galat (Error): Program otomatis berhenti (konvergen) ketika nilai galat hampiran lebih kecil dari batas toleransi yang ditetapkan (< 0.0001).

Alur Logika (Flowchart)
(Flowchart/Diagram Tanpa Judul.drawio.png)

Cara Menjalankan Program:
Pastikan Python 3.x sudah terpasang di komputermu.

1. Clone repositori ini ke komputer lokal:
git clone https://github.com/username-kamu/nama-repo-kamu.git

2. Masuk ke direktori proyek:
cd nama-repo-kamu

3. Jalankan script Python:
python newton_raphson.py

Identitas Pembuat:
- Phiong Herson
- Febryadie
