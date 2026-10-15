# Program kalkulator sederhana

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak dapat membagi dengan nol"

def menu():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

def main():
    while True:
        menu()
        
        pilihan = input("Masukkan pilihan (1/2/3/4) atau 'keluar' untuk keluar: ")
        
        if pilihan.lower() == 'keluar':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                x = float(input("Masukkan angka pertama: "))
                y = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
                continue
            
            if pilihan == '1':
                print(f"Hasil: {tambah(x, y)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(x, y)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(x, y)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(x, y)}")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

