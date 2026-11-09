try:
    hari = input("Ketik (1 = hari Kerja), (2 = akhir pekan) = ")
except ValueError:
    print("Input tidak valid. Harap masukkan angka 1 atau 2.")
    exit()
jumlah_tiket = int(input("Masukkan jumlah tiket = "))

if hari == "1":
    total = jumlah_tiket * 35000
    if jumlah_tiket >= 5:
        total = total - (total * 10/100)

elif hari == "2":
    total = jumlah_tiket * 50000
    if jumlah_tiket >= 5:
        total = total - (total * 5/100)

print("Total harga tiket yang harus dibayar adalah Rp", total)