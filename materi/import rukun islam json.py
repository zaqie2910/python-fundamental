import json

# Membaca file rukun_islam.json
with open('rukun_islam.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

# Menampilkan isi file
print("Judul:", data.get('judul'))
print("Jumlah:", data.get('jumlah'))
print("Rukun:", data.get('rukun'))
print("Surah:")
for surah in data.get('surah', []):
	print(f"  - {surah['nama']} ({surah['ayat']} ayat, turun di {surah['turun']})")
