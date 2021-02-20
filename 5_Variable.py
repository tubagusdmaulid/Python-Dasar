# Variable = tempat menyimpan data

# Teknik penulisan variable
# camelCase
namaSaya = "Tubagus"  # String
umurSaya = 21  # int
nilaiUN = 92.8  # float

# PascalCase
NamaSaya = "Tubagus"  # String
UmurSaya = 21  # int
NilaiUn = 92.8  # float

# snake_case
nama_saya = "Tubagus"  # String
umur_saya = 21  # int
nilai_un = 92.8  # float

# Nilai variable
a = 1  # 1 nilai utk 1 variable
b, c, d = 2, 3, 4  # banyak nilai utk banyak variable
e = f = g = 10  # 1 nilai utk banyak variable
print(a)
print(b)
print(e)

# cek tipe data variable
print(type(namaSaya))  # String
print(type(umurSaya))  # int
print(type(nilaiUN))  # float

# Variable global
global x

x = "x adalah variable global"
print(x)
