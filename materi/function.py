print("===== MATERI 9 - PYTHON FUNCTION =====")
print("=====================================\n")

# Fungsi biasa dengan def
def hello_world(name):
    print("Hallo", name)
    print("Apa kabar?")

hello_world("Ali")
hello_world("Azka")
hello_world("Haris")

print("\n--------> LAMBDA <--------")

# Fungsi anonim dengan lambda (1 baris)
greeting = lambda name: print(f"Hello, {name}! Selamat datang 🙌")
greeting("Azmi")
greeting("Zaky")
greeting("Karim")

print("\n--------> CONVERSI TIPE DATA <--------")
nilai_string = "1000"
nilai_integer = int(nilai_string)
print("String:", nilai_string, "| Integer:", nilai_integer)

# Lambda untuk operasi matematika singkat
kalikan_dua = lambda x: x * 2
print("5 x 2 =", kalikan_dua(5))
print("12 x 2 =", kalikan_dua(12))

print("\n--------> MAP() <--------")
# map() untuk mentransformasi data
nilai_mentah = [7.5, 8.1, 6.4, 9.9, 10.0]
nilai_dibulatkan = list(map(lambda n: round(n), nilai_mentah))
nilai_kali_seratus = list(map(lambda n: n * 100, nilai_mentah))

print("Nilai mentah     :", nilai_mentah)
print("Nilai dibulatkan :", nilai_dibulatkan)
print("Nilai x100       :", nilai_kali_seratus)

print("\n--------> FILTER() <--------")
# filter() menyaring data
transaksi = [5000, 18000, 13000, 10000, 125000]
transaksi_besar = list(filter(lambda angka: angka >= 25000, transaksi))

print("Data transaksi        :", transaksi)
print("Transaksi >= 25.000   :", transaksi_besar)
