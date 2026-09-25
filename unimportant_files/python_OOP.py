

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    @classmethod
    def mengisi(cls):
        nama = input("Nama anda : ")
        nim = input("Nim anda : ")
        jurusan = input("Jurusan anda : ")
        return cls(nama, nim, jurusan)

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")

class Dosen:
    def __init__(self, nama, nip, mata_kuliah):
        self.nama = nama
        self.nip = nip
        self.mata_kuliah = mata_kuliah

    @classmethod
    def mengisi(cls):
        nama = input("Nama anda : ")
        nip = input("NIP anda : ")
        mata_kuliah = input("Mata kuliah anda : ")
        return cls(nama, nip, mata_kuliah)

    def tampilkan_info(self):
        print(f"Nama        : {self.nama}")
        print(f"NIP         : {self.nip}")
        print(f"Mata Kuliah : {self.mata_kuliah}")


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def choice():
        print("Hello, Nigga. How are you today?")
        print("++++++++++++++++++++++++++++++++")
        print("You can choose here: ")
        print("1. Dosen")
        print("2. Mahasiswa")
        pilihan = input("Choose it one: ")
        if pilihan == "1":
            dosen = Dosen.mengisi()
            dosen.tampilkan_info()
        elif pilihan == "2":
            mahasiswa = Mahasiswa.mengisi()
            mahasiswa.tampilkan_info()

while True:
    Menu.choice()
    

