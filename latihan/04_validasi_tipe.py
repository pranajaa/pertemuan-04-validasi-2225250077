teks = input("Jumlah soal benar dari 20: ") .strip()

try:
    benar = int(teks)
except ValueError:
    print("Masukan tidak valid. Harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("Masukan tidak valid. Jumlah harus berada di antara 0 dan 20.")
    else:
        persen = benar / 20 * 100
        print(f"Persentase = {persen: .2f} %")
        if persen >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")