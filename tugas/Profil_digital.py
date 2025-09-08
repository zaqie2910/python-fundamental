print("===== PROFIL DIGITAL======")
nama = input("nama: ")
umur = int(input("umur: "))
kelas = int(input("kelas: "))
cita2 = input("cita cita: ")
hobi = input("hobi: ")
waktu_belajar = input("lebih enak belajar malem ato pagi: ")

tahun_lahir = 2025 - umur  # otomatis hitung tahun lahir

print("\n=====TYPE DIGITAL=====")
print("1. wibu")
print("2. gamer")
print("3. k-popers")
print("4. anak nongki")
print("5. anak konten")

tipe = int(input("apa tipe kamu? "))
tambahan = ""

if tipe == 1:
    tambahan = input("siapa nama waifu kamu? ")
elif tipe == 2:
    tambahan = input("apa game favorit kamu? ")
elif tipe == 3:
    tambahan = input("siapa bias kamu? ")
elif tipe == 4:
    tambahan = input("platform favorit kamu apa? youtube? tiktok? ")
elif tipe == 5:
    tambahan = input("nongkrong paling seru dimana? ")
else:
    print("pilihan tidak valid, silahkan isi angka 1-5")

print("\n===== PROFIL DIGITAL KAMU =====")
print(f"nama: {nama}")
print(f"umur: {umur} tahun")
print(f"kelas: {kelas}")
print(f"cita-cita: {cita2}")
print(f"hobi: {hobi}")
print(f"belajar paling enak: {waktu_belajar}")
print(f"tahun lahir: {tahun_lahir}")

print("\n===== TIPE DIGITAL=====")
print(f"tipe: {tipe}")
print(f"detail: {tambahan}")

print("\n==== CHEK BERCANDA ====")
teman_bau = input("teman sebelah bau? (iya/tidak) ")
reaksi = input("kalau iya/tidak, reaksi kamu apa? ")
print(f"teman sebelah bau? {teman_bau}")
print(f"reaksi kamu: {reaksi}")

print("===================")
