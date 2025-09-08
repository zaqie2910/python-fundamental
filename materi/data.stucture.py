print("===== MATERI 7B - PYTHON DATA STRUCTURE =====")
print("============================================\n")

# SET -> { } -> tidak berurutan, bisa berubah, tidak duplikat
game_azka = {"valorant", "dark soul"}
game_evan = {"genshin", "MLBB"}

print("Awal koleksi games:")
print("Azka games :", game_azka)
print("Evan games :", game_evan)

# .add() -> menambahkan item baru
game_azka.add("elden ring")
game_azka.add("valorant")  # tidak bertambah karena sudah ada

# .remove() -> menghapus item
game_evan.remove("MLBB")

# len() menghitung jumlah item
print("\nSetelah update:")
print("Azka punya", len(game_azka), "games :", game_azka)
print("Evan punya", len(game_evan), "games :", game_evan)

# .union() -> menggabung 2 set
game_berdua = game_azka.union(game_evan)
print("\nGabungan games berdua:", len(game_berdua), "games :", game_berdua)

# .intersection() -> mencari item yg sama
# .difference() -> mencari item yg beda
game_kembar = game_azka.intersection(game_evan)
game_beda = game_azka.difference(game_evan)

print("Games yang sama/kembar :", len(game_kembar), "->", game_kembar)
print("Games yang beda (punya Azka aja) :", len(game_beda), "->", game_beda)

# =====================================================
# DICTIONARY -> { key: value }
koleksi_anime = {
    "re_zero": "subaru",
    "onePiece": "usop",
    "waifu": {
        "re_zero": "rem-chan",
        "demon_slayer": "nezuko",
    }
}

print("\n===== KOLEKSI ANIME =====")
print("Awal koleksi:", koleksi_anime)
print("MC One Piece:", koleksi_anime["onePiece"])

# menambah atau mengubah data dict
koleksi_anime["naruto"] = "boruto"           # tambah baru
koleksi_anime["onePiece"] = "zoro"           # update value
koleksi_anime["waifu"]["re_zero"] = "rem kanan"  # update nested dict

print("Update koleksi anime:", koleksi_anime)
print("MC One Piece sekarang:", koleksi_anime["onePiece"])
print("Waifu Re:Zero sekarang:", koleksi_anime["waifu"]["re_zero"])