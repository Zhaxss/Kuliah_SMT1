print('-------------start x ---------------')
print('Contoh perulangan 1')
for nomor in range(5):
    print(nomor)

print('-----------------------------')
print('Contoh perulangan 2')
for nomor in range(1,6):
    print(nomor)

print('-----------------------------')
print('Contoh perulangan 3')
for nomor in range(2,11,2):
    print(nomor)

print('-----------------------------')
print('Contoh perulangan 4')
for nomor in range(5, 0, -1):
    print(nomor)

print('-----------------------------')
print('Contoh perulangan 5')
for nomor in range(1,4):
    hasil = nomor * 2
    print(nomor)

print('-----------------------------')
print('Contoh perulangan 6')
for nomor in range(4):
    print('Dalam',nomor)
print('Luar', nomor)

print('-----------------------------')
print('Contoh perhitungan')
perhitungan = 0
for nomor in range(1,6):
    perhitungan = perhitungan + 2
    print(perhitungan)

print('-----------------------------')
print('Contoh akumulator')
total = 0
for nomor in range(1,6):
    total = total + nomor 
    print(total)

print('-----------------------------')
print('Contoh Kasus Bilangan Genap 1 - 20')
genap = 0
for nomor in range(1,20, 2):
    genap = genap + 2
    print(genap)

print('-----------------------------')
print('Contoh Kasus Bilangan Genap 1 - 20')
for nomor in range(2,22, 2):
    print(nomor)
print('-------------end---------------')