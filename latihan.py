kwh = int(input("Masukkan jumlah kWh yang digunakan = "))

if kwh <= 100:
    tarif = kwh * 1500
elif kwh > 100:
    tarif = 100 * 1500 + (kwh - 100) * 2000
    if tarif > 300000:
        tarif = tarif + 15000
print("Total tagihan listrik yang harus dibayar adalah Rp", tarif)