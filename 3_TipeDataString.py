# single Line
print('Penulisan String dengan petik 1')
print("Penulisan String dengan petik 2")

# New Line (\n = enter)
print("Baris pertama \nBaris kedua")

# Multi line
print("""Baris pertama 
Baris kedua
Baris ketiga""")

# Varibale string
nama = "Tubagus Dinda Maulid"
print(nama)  # Output : Tubagus Dinda Maulid
print(nama[1])  # Output indeks 1 : U
print(nama[2:6])  # Output indeks 2 - 6 : bagus
print(nama[:7])  # Output indeks 0-6 : tubagus
print(nama[2:])  # Output indeks 2 - akhir : bagus Dinda Maulid

# String Format
namaDepan = "Tubagus"
namaTengah = "Dinda"
namaBelakang = "Maulid"
umur = 21
teks = f"Hai!, nama saya {namaDepan} {namaTengah} {namaBelakang}, umur saya {umur} tahun"
print(teks)

# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
#Silahkan baca sendiri string method
namaLengkap = "tubagus DINDA maulid"
print(namaLengkap)
print(namaLengkap.upper())  # Huruf kapital : TUBAGUS DINDA MAULID
print(namaLengkap.lower())  # Huruf kecil : tubagus dinda maulid
print(namaLengkap.capitalize())  # Huruf awal kapital : Tubagus dinda maulid
print(namaLengkap.title())  # awal kata kapital : Tubagus Dinda Maulid
print(namaLengkap.split(" "))  # Daftar kata : ['tubagus','dinda','maulid']
