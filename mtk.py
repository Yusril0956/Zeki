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
        return "Tidak bisa membagi dengan nol!"

while True:
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan in ['1', '2', '3', '4']:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print("Hasil: ", tambah(angka1, angka2))
        elif pilihan == '2':
            print("Hasil: ", kurang(angka1, angka2))
        elif pilihan == '3':
            print("Hasil: ", kali(angka1, angka2))
        elif pilihan == '4':
            print("Hasil: ", bagi(angka1, angka2))
    elif pilihan == '5':
        print("Terima kasih! Sampai jumpa lagi.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
