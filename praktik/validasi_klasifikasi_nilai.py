print("Validasi Klasifikasi Nilai Akhir")

teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan tidak valid. Harus berupa angka.")
else:
    if not (0 <= ujian <= 100):
        print("Masukan tidak valid. Nilai ujian diluar rentang 0-100.")
    elif not (0 <= tugas <= 100):
        print("Masukan tidak valid. Nilai tugas diluar rentang 0-100.")
    elif not (0 <= hadir <= 100):
        print("Masukan tidak valid. Kehadiran diluar rentang 0-100.")
    else:
        #Nilai akhir
        nilai_akhir = (0.6 * ujian) + (0.4 * tugas)

        #Syarat kehadiran
        if hadir < 80:
            predikat = "-"
            status = "Tidak memenuhi syarat kehadiran"
        else:
            #Predikat
            if nilai_akhir >= 85:
                predikat = "A"
            elif nilai_akhir >= 70:
                predikat = "B"
            elif nilai_akhir >= 60:
                predikat = "C"
            elif nilai_akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"

            #Status kelulusan
            if predikat in ["A", "B", "C"]:
                status = "Lulus"
            else:
                status = "Belum Lulus"

            #Hasil
        print(f"Nilai akhir: {nilai_akhir:.2f}")
        print(f"Predikat: {predikat}")
        print(f"Status: {status}")