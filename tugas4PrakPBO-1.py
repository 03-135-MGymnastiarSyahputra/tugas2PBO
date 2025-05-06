import math  # Mengimpor modul math untuk menggunakan fungsi sqrt

# Kelas utama untuk menghitung akar kuadrat
class AkarKuadratCalculator:
    def __init__(self):
        # Konstruktor untuk menginisialisasi atribut angka
        self.angka = None

    def masukkan_angka(self):
        # Fungsi untuk meminta input angka dari pengguna dan memvalidasinya
        while True:
            try:
                # Input dari pengguna
                user_input = input("Masukkan angka: ")
                self.angka = float(user_input)  # Konversi ke float

                # Cek apakah angka <= 0
                if self.angka <= 0:
                    # Jika nol, tampilkan pesan error khusus
                    raise ValueError("Akar kuadrat dari nol tidak diperbolehkan." 
                                     if self.angka == 0 else 
                                     "Input tidak valid. Harap masukkan angka yang positif.")
                break  # Keluar dari loop jika input valid

            except ValueError as e:
                # Tangani input yang tidak valid (bukan angka atau angka <= 0)
                if "could not convert" in str(e):
                    print("Input tidak valid. Harap masukkan angka yang valid.")
                else:
                    print(f"Error: {e}")

    def hitung_akar_kuadrat(self):
        # Fungsi untuk menghitung akar kuadrat dari angka yang sudah divalidasi
        hasil = math.sqrt(self.angka)  # Menghitung akar kuadrat
        print(f"Akar kuadrat dari {int(self.angka)} adalah {hasil:.1f}")  # Tampilkan hasil dengan 1 desimal

# Fungsi utama sebagai titik masuk program
if __name__ == "__main__":
    kalkulator = AkarKuadratCalculator()  # Membuat objek kalkulator
    kalkulator.masukkan_angka()           # Meminta dan memvalidasi input
    kalkulator.hitung_akar_kuadrat()      # Menghitung dan menampilkan hasil akar kuadrat
