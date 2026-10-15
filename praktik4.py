# while True:
#     try:
#         x = float(input('Masukkan Nilai X : '))
#         y = float(input('Masukkan Nilai Y : '))
#         break     
#     except ValueError:
#         print('Silahkan Masukkan Nilai Yang benar')
#     continue

# if x > y:
#     print('X Lebih besar dari Y')
# else: 
#     print('X tidak lebih besar dari Y')



while True:
    try:
        x = int(input('Masukkan Nilai X : '))
        break     
    except ValueError:
        print('Silahkan Masukkan Kembali Nilai Yang benar')
    continue

if x % 2 == 0:
    print('X = Genap')
else: 
    print('X = Ganjil')