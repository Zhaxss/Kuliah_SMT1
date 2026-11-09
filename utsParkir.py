waktu = int(input("Masukkan waktu parkir (dalam jam) = "))

if waktu <= 2:
    tarif = 5000
elif waktu <= 5:
    tarif = 5000 + (waktu - 2) * 3000
else:
    tarif = 5000 + (3 * 3000) + (waktu - 5) * 2000

print("Tarif parkir yang harus dibayar adalah Rp", tarif)