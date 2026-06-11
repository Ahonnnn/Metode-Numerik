# Program: Penentuan Titik Impas (BEP) UMKM
# Metode: Newton-Raphson

def f(x):
    """Fungsi Keuntungan UMKM"""
    return -0.5 * x**3 + 4 * x**2 - 2 * x - 5

def df(x):
    """Turunan Pertama dari Fungsi Keuntungan"""
    return -1.5 * x**2 + 8 * x - 2

def newton_raphson(x0, tol=0.0001, max_iter=20):
    print("=" * 60)
    print(f"{'Iter':<5} | {'x_n':<12} | {'f(x_n)':<12} | {'Galat (Error)':<15}")
    print("-" * 60)

    x_n = x0
    
    for i in range(1, max_iter + 1):
        fx = f(x_n)
        dfx = df(x_n)

        # Mencegah error pembagian dengan nol (Math Error)
        if dfx == 0:
            print("Turunan f'(x) bernilai nol. Iterasi dihentikan.")
            break

        # Rumus utama Newton-Raphson
        x_next = x_n - (fx / dfx)
        
        # Menghitung galat (selisih nilai x baru dan x lama)
        error = abs(x_next - x_n)

        # Menampilkan hasil tiap iterasi ke dalam tabel
        print(f"{i:<5} | {x_n:<12.5f} | {fx:<12.5f} | {error:<15.5f}")

        # Cek apakah galat sudah lebih kecil dari toleransi yang diizinkan
        if error < tol:
            print("-" * 60)
            print(f"Berhasil konvergen pada iterasi ke-{i}!")
            print(f"Titik Impas (x) ditemukan di: {x_next:.5f}")
            print("=" * 60)
            return x_next

        # Update nilai x untuk iterasi selanjutnya
        x_n = x_next

    print("Iterasi maksimum tercapai, akar belum konvergen.")
    return None

# --- Bagian Utama Program ---
if __name__ == "__main__":
    print("PROGRAM ANALISIS TITIK IMPAS PRODUKSI UMKM")
    print("Persamaan: f(x) = -0.5x^3 + 4x^2 - 2x - 5")
    print("")
    
    # Menjalankan fungsi dengan tebakan awal x0 = 1
    tebakan_awal = 1.0
    newton_raphson(x0=tebakan_awal)