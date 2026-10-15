while True:
    try:
        nilai = int(input('Masukkan Nilai : '))
        break     
    except ValueError:
        print('Silahkan Masukkan Kembali Nilai Yang benar')
    continue

if nilai >= 81 and nilai <= 100:
    print('Nilai A')
elif nilai >= 77 and nilai < 81:
    print('Nilai A-')
elif nilai >= 73 and nilai < 77:
    print('Nilai B+')   
elif nilai >= 70 and nilai < 73:
    print('Nilai B')
elif nilai >= 66 and nilai < 70:
    print('Nilai B-')
elif nilai >= 56 and nilai < 66:
    print('Nilai C+')
elif nilai >= 56 and nilai < 62:
    print('Nilai C')
elif nilai >= 52 and nilai < 56:
    print('Nilai C-')
elif nilai >= 46 and nilai < 52:
    print('Nilai D')
else:
    print('Nilai E')
