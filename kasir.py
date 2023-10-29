total = 0
barang = []
harga = []

while True:
    print("""DAFTAR MENU \n
1. Nasi \t 5000
2. Ayam \t 7000
3. Soup \t 4000
4. ESteh \t 3000
""")
    kode = float(input("Masukan kode Menu: "))
    if kode == 1:
        barang.append('Nasi')
        harga.append('5000')
        total += 5000
    elif kode == 2:
        barang.append('Ayam')
        harga.append('7000')
        total += 7000
    elif kode == 3:
        barang.append('Soup')
        harga.append('4000')
        total += 4000
    elif kode == 4:
        barang.append('ESteh')
        harga.append('3000')
        total += 3000
    else:
        print("Kode tidak valid")

    lanjut = input('Ingin lanjut? (y/t)', )
    print('')
    if lanjut == 't':
        break          

print('Barang yang di beli: ', barang)
print('Harga barang: ', harga)
print('Total harga: ', total, '\n')

uang = float(input('Uang pembayaran: '))
if uang > total:
    print('Kembalian: ', total-uang)
elif uang == total:
    print('Uang Pas')
else:
    print('Uang kurang ', uang - total)