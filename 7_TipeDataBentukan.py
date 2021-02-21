# Tipe data bentukan
# Ada 4 dengan perbedaan:
# 1. List = data terurut, dapat diubah, data bisa sama
# 2. Tuple = data terurut, tidak dapat diubah, data bisa sama
# 3. Set = data tidak terurut, tidak terindeks, data unik
# 4. Dictionary = data tidak terurut, dapat diubah, data unik

# List
listKeranjang = ["Apel", "Mangga", "Jeruk", "Apel", 1000, 2000, 5000]
print(listKeranjang)  # Output listKeranjang
print(listKeranjang[2])  # Akses indeks, Output: jeruk

listKeranjang.append("Anggur")  # Tambah data
print(listKeranjang)

listKeranjang.remove("Mangga")  # Hapus data (indeks ikut geser)
print(listKeranjang)

print(len(listKeranjang))  # Ukuran list

# Tuple
tupleHewan = ("Singa", "Ayam", "Kambing", "Kambing")
print(tupleHewan)  # output tuple
print(tupleHewan[2])  # Akses indeks

# tupleHewan.append("Ular") Tidak bisa menambah
# tupleHewan.remove("Singa") Tidak bisa menghapus

print(len(tupleHewan))  # Ukuran tuple

# Set
setSiswa = {"Budi", "Eko", "Tubagus", "Budi"}
print(setSiswa)  # Output Set , data unik 2 Budi dianggap 1

# Tidak bisa akses indek, alternatif pakai looping
for nama in setSiswa:
    print(nama)

setSiswa.add("Dinda")  # Menambah data
print(setSiswa)
setSiswa.remove("Budi")  # Menghapus data
print(setSiswa)

# Dictionary
dictionaryData = {"nama": "Tubagus", "Age": 21, "Address": "Lampung"}
print(dictionaryData)  # output dictionary

for key in dictionaryData:  # Ouput pakai looping
    value = dictionaryData[key]
    print(f"{key} : {value}")


dictionaryData["Email"] = "tb@gmail.com"  # Tambah data
for key, value in dictionaryData.items():
    print(f"{key} : {value}")


del dictionaryData["Email"]  # Hapus data
print(dictionaryData)
