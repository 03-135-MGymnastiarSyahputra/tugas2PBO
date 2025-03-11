# Kelas Induk Kendaraan
class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        return f"Jenis Kendaraan: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam"

    def bergerak(self):
        return f"Kendaraan sedang bergerak."


# Kelas Turunan Mobil
class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        return f"{self.info_kendaraan()}, Merek: {self.merk}, Jumlah Pintu: {self.jumlah_pintu}"

    def bunyikan_klakson(self):
        return "BEEP BEEP!"


# Kelas Turunan MobilSport
class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda  # Private property
        self.__harga = harga  # Private property

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus positif.")

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus positif.")

    def info_mobil_sport(self):
        return f"{self.info_mobil()}, Tenaga Kuda: {self.get_tenaga_kuda()}, Harga: {self.get_harga()} juta rupiah"

    def mode_balap(self):
        return "Mobil sport masuk ke mode balap!"


# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek dari kelas MobilSport
    mobil_sport = MobilSport("Darat", 300, "Ferrari", 2, 600, 5000)

    # Menampilkan informasi mobil sport
    print(mobil_sport.info_mobil_sport())
    print(mobil_sport.bergerak())
    print(mobil_sport.bunyikan_klakson())
    print(mobil_sport.mode_balap())

    # Mengubah tenaga kuda dan harga
    mobil_sport.set_tenaga_kuda(650)
    mobil_sport.set_harga(5500)

    # Menampilkan informasi setelah perubahan
    print(mobil_sport.info_mobil_sport())