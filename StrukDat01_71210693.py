print("Aplikasi Kalkulator Sederhana Operasi Dua Bilangan")
print("1. Operasi penjumlahan (+)")
print("2. Operasi pengurangan (-)")
print("3. Operasi perkalian (*)")
print("4. Operasi pembagian (/)")
print("5. Matikan Aplikasi (Tekan Q)")
print()
print("Contoh penulisan: 4 + 2")

while True:
    hitung = input("Masukkan operasi perhitungan: ")
    x = hitung.split()
    if hitung == "Q" :
        break
    elif "+" in x :
        tambah = int(x[0]) + int(x[2])
        print(f"Hasil penjumlahan = {tambah}")
    elif "-" in x :
        kurang = int(x[0]) - int(x[2])
        print(f"Hasil pengurangan = {kurang}")
    elif "*" in x :
        kali = int(x[0]) * int(x[2])
        print(f"Hasil perkalian = {kali}")
    elif "/" in x :
        bagi = int(x[0]) / int(x[2])
        print(f"Hasil pembagian = {bagi}")
    else:
        print("Operasi tidak valid!")






