from datetime import datetime
import json

print("Selamat Datang Di Apotek Alif Farma")
riwayat_pembelian = []
stok_barang = {
    "asam mefenamat": 50,
    "amoxicillin": 30,
    "reserpinum": 20,
    "Madu Herbal": 40,
    "Imboost": 25,
    "Stimuno": 15,
    "Paracetamol": 100,
    "Aspirin 500 mg": 80,
    "Komix": 60,
    "Masker": 200,
    "Termometer": 10,
    "Tensimeter": 5
}
pilihan = "ya"
while pilihan.lower() == "ya":
    
    nama = input("Masukkan Nama Anda: ")

    print("|=======================================|")
    print("|    Kategori barang yang tersedia:     |")
    print("|=======================================|")
    print("| 1. Obat                               |")
    print("| 2. Alat Kesehatan                     |")
    print("|=======================================|")
    kategori = input("Masukkan pilihan barang yang ingin Anda beli (1/2) = ")

    if kategori == "1":
        print("|=======================================|")
        print("|        Jenis obat yang tersedia:      |")
        print("|=======================================|")
        print("| 1. Keras                              |")
        print("| 2. Herbal                             |")
        print("| 3. Bebas                              |")
        print("|=======================================|")
        obat = input("Masukkan pilihan jenis obat yang ingin Anda beli (1/2/3) = ")

        if obat == "1":
            print("|=============================================|")
            print("|          Obat Keras yang tersedia:          |")
            print("|=============================================|")
            print("|       Nama obat   |   Harga   |    Stok     |")
            print("|=============================================|")
            print(f"| 1. asam mefenamat | Rp. 10000 |    {stok_barang['asam mefenamat']}       |")
            print(f"| 2. amoxicillin    | Rp. 20000 |    {stok_barang['amoxicillin']}       |")
            print(f"| 3. reserpinum     | Rp. 30000 |    {stok_barang['reserpinum']}       |")
            print("|=============================================|")
            pilihan_obat = input("Masukkan pilihan obat (1/2/3) = ")

            if pilihan_obat == "1":
                nama_barang = "asam mefenamat"
                harga = 10000
            elif pilihan_obat == "2":
                nama_barang = "amoxicillin"
                harga = 20000                
            elif pilihan_obat == "3":
                nama_barang = "reserpinum"
                harga = 30000               
            else:
                print("Pilihan tidak valid.")
                continue

        elif obat == "2":
            print("|=============================================|")
            print("|        Obat Herbal yang tersedia:           |")
            print("|=============================================|")
            print("|    Nama obat   |   Harga   |      Stok      |")
            print("|=============================================|")
            print(f"| 1. Madu Herbal | Rp. 15000 |      {stok_barang['Madu Herbal']}        |")
            print(f"| 2. Imboost     | Rp. 25000 |      {stok_barang['Imboost']}        |")
            print(f"| 3. Stimuno     | Rp. 35000 |      {stok_barang['Stimuno']}        |")
            print("|=============================================|")
            pilihan_obat = input("Masukkan pilihan obat (1/2/3) = ")

            if pilihan_obat == "1":
                nama_barang = "Madu Herbal"
                harga = 15000              
            elif pilihan_obat == "2":
                nama_barang = "Imboost"
                harga = 25000               
            elif pilihan_obat == "3":
                nama_barang = "Stimuno"
                harga = 35000                
            else:
                print("Pilihan tidak valid.")
                continue

        elif obat == "3":
            print("|=============================================|")
            print("|        Obat Bebas yang tersedia:            |")
            print("|=============================================|")
            print("|    Nama obat      |   Harga   |    Stok     |")
            print("|=============================================|")
            print(f"| 1. Paracetamol    | Rp. 5000  |     {stok_barang['Paracetamol']}     |")
            print(f"| 2. Aspirin 500 mg | Rp. 10000 |     {stok_barang['Aspirin 500 mg']}      |")
            print(f"| 3. Komix          | Rp. 15000 |     {stok_barang['Komix']}      |")
            print("|=============================================|")
            pilihan_obat = input("Masukkan pilihan obat (1/2/3) = ")

            if pilihan_obat == "1":
                nama_barang = "Paracetamol"
                harga = 5000               
            elif pilihan_obat == "2":
                nama_barang = "Aspirin 500 mg"
                harga = 10000               
            elif pilihan_obat == "3":
                nama_barang = "Komix"
                harga = 15000                
            else:
                print("Pilihan tidak valid.")
                continue

        else:
            print("Jenis obat tidak valid.")
            continue

    elif kategori == "2":
        print("|=============================================|")
        print("|        Alat Kesehatan yang tersedia:        |")
        print("|=============================================|")
        print("|  Nama barang  |   Harga    |     Stok       |")
        print("|=============================================|")
        print(f"| 1. Masker     | Rp. 2000   |     {stok_barang['Masker']}        |")
        print(f"| 2. Termometer | Rp. 50000  |     {stok_barang['Termometer']}         |")
        print(f"| 3. Tensimeter | Rp. 250000 |     {stok_barang['Tensimeter']}          |")
        print("|=============================================|")
        pilihan_alat = input("Masukkan pilihan alat kesehatan (1/2/3) = ")

        if pilihan_alat == "1":
            nama_barang = "Masker"
            harga = 2000
        elif pilihan_alat == "2":
            nama_barang = "Termometer"
            harga = 50000
        elif pilihan_alat == "3":
            nama_barang = "Tensimeter"
            harga = 250000
        else:
            print("Pilihan tidak valid.")
            continue

    else:
        print("Kategori tidak valid.")
        continue

    jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))

    if jumlah > stok_barang[nama_barang]:
        print("Stok tidak mencukupi")
        continue

    total_harga = harga * jumlah
    tanggal = datetime.now().strftime ('%Y-%m-%d %H:%M:%S')
    
    stok_barang[nama_barang] -= jumlah 

    print("======================= STRUK PEMBELIAN =====================")
    print(f"Tanggal dan waktu : {tanggal}")
    print("===============================================================")
    print(f"Nama Barang  : {nama_barang}")
    print(f"Jumlah       : {jumlah}")
    print(f"Harga Satuan : Rp. {harga}")
    print(f"Total Harga  : Rp. {total_harga}")
    print("===============================================================")

    uang_dibayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
    if uang_dibayar < total_harga:
        print("Uang tidak mencukupi, anda tidak bisa membeli barang ini")
        break

    kembalian = uang_dibayar - total_harga  
    print(f"Uang Dibayar : Rp. {uang_dibayar}")
    print(f"Kembalian    : Rp. {kembalian}")
    print("===============================================================")

    riwayat_pembelian.append({
        "tanggal": tanggal,
        "nama_barang": nama_barang,
        "jumlah": jumlah, 
        "harga_satuan": harga,
        "total_harga": total_harga,
        
        "uang_dibayar": uang_dibayar,
        "kembalian": kembalian
})

    pilihan = input("Apakah Anda ingin membeli barang lain? (ya/tidak): ")

    with open("riwayat_pembelian.json", "w") as file:
        json.dump(riwayat_pembelian, file, indent=4)

print(f"Terima kasih telah berbelanja di Apotek Alif Farma! {nama}")

