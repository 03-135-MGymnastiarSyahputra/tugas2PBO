# Exception kustom untuk menangani error khusus dalam manajemen tugas
class TodoError(Exception):
    pass

# Kelas utama untuk manajemen daftar tugas
class TodoList:
    def __init__(self):
        # Inisialisasi daftar tugas sebagai list kosong
        self.tugas = []

    def tambah_tugas(self, tugas):
        # Fungsi untuk menambahkan tugas ke daftar
        if not tugas.strip():
            # Cek apakah input kosong atau hanya spasi
            raise TodoError("Tugas tidak boleh kosong.")
        self.tugas.append(tugas)
        print(f"Tugas berhasil ditambahkan!\n")

    def hapus_tugas(self, nomor):
        # Fungsi untuk menghapus tugas berdasarkan nomor urutan
        if nomor < 1 or nomor > len(self.tugas):
            # Jika nomor di luar jangkauan daftar tugas
            raise TodoError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        tugas_dihapus = self.tugas.pop(nomor - 1)
        print(f"Tugas '{tugas_dihapus}' dihapus.\n")

    def tampilkan_tugas(self):
        # Fungsi untuk menampilkan seluruh daftar tugas
        print("Daftar Tugas:")
        if not self.tugas:
            # Jika daftar kosong
            print("- Tidak ada tugas.")
        else:
            for idx, tugas in enumerate(self.tugas, 1):
                print(f"- {tugas}")
        print()

# Kelas aplikasi utama yang mengatur interaksi pengguna
class TodoApp:
    def __init__(self):
        # Inisialisasi aplikasi dengan objek TodoList
        self.todo_list = TodoList()

    def tampilkan_menu(self):
        # Fungsi untuk menampilkan menu utama ke pengguna
        print("Pilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

    def mulai(self):
        # Fungsi utama yang menjalankan aplikasi
        while True:
            self.tampilkan_menu()
            try:
                # Menerima input pilihan aksi dari user
                pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
                print()
                if pilihan == 1:
                    # Tambah tugas
                    tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                    self.todo_list.tambah_tugas(tugas)
                elif pilihan == 2:
                    # Hapus tugas
                    if not self.todo_list.tugas:
                        print("Tidak ada tugas untuk dihapus.\n")
                        continue
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    self.todo_list.hapus_tugas(nomor)
                elif pilihan == 3:
                    # Tampilkan semua tugas
                    self.todo_list.tampilkan_tugas()
                elif pilihan == 4:
                    # Keluar dari program
                    print("Keluar dari program.")
                    break
                else:
                    # Pilihan di luar 1-4
                    print("Pilihan tidak valid. Silakan pilih 1-4.\n")
            except ValueError:
                # Menangani jika input bukan angka
                print("Input tidak valid. Masukkan angka 1-4.\n")
            except TodoError as e:
                # Menangani error kustom dari TodoList
                print(f"Error: {e}\n")

# Menjalankan program
if __name__ == "__main__":
    app = TodoApp()
    app.mulai()
