print("===== Materi 8 - Function Dasar =====")
print("====================================\n")

# Fungsi tanpa parameter
def hallo_dunia():
    print("Hello World!")
    print("Halo Dunia!")

# cara akses function, sertakan nama + ()
hallo_dunia()

print("\n===== Fungsi dengan Parameter =====")

# Fungsi dengan parameter
def sapa_sapa_gan(nama):
    print("Hallo", nama, "selamat datang di HSI")

# Fungsi menghitung luas segitiga
def rumus_luas_segitiga(alas, tinggi):
    print("\nMenghitung luas segitiga:")
    print("Alas   :", alas)
    print("Tinggi :", tinggi)
    rumusan = 1/2 * (alas * tinggi)
    print("Hasil  :", rumusan)

# Panggil fungsi sapa
sapa_sapa_gan("Ujang")
sapa_sapa_gan("Asep")

# Manual (tanpa fungsi) biar keliatan bedanya
print("Halo Ujang selamat datang di HSI")
print("Hallo Asep selamat datang di HSI")

# Panggil fungsi rumus
rumus_luas_segitiga(10, 30)
rumus_luas_segitiga(50, 100)
rumus_luas_segitiga(7, 15)