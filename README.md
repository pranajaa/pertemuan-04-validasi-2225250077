# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input
Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else

## Cara Menjalankan
### Latihan
python3 latihan/01_predikat_nilai.py

python3 latihan/02_kategori_bilangan.py

python3 latihan/03_validasi_rentang.py

python3 latihan/04_validasi_tipe.py

python3 latihan/05_klasifikasi_segitiga_sudut.py

### Praktik
python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan

| Kategori | Syarat | Contoh Masukan |
|---|---|---|
| Predikat A | Nilai akhir >= 80 | Ujian 90, Tugas 80 |
| Predikat B | Nilai akhir >= 70 | Ujian 75, Tugas 70 |
| Predikat C | Nilai akhir >= 60 | Ujian 60, Tugas 60 |
| Predikat D | Nilai akhir >= 50 | Ujian 55, Tugas 50 |
| Predikat E | Nilai akhir < 50 | Ujian 40, Tugas 30 |
| Kehadiran diluar rentang | Kehadiran < 80% | Kehadiran 75 |
| Nilai ujian diluar rentang | Nilai ujian < 0 atau > 100 | Ujian 105 |
| Nilai tugas diluar rentang | Nilai tugas < 0 atau > 100 | Tugas -5 |
| Masukan tidak valid | Input bukan angka | Kehadiran abc |

## Hasil Pengujian

| Ujian | Tugas | Kehadiran | Nilai Akhir | Keluaran yang Diharapkan |
|---:|---:|---:|---:|---|
| 90 | 80 | 95 | 86.00 | Predikat A, Lulus |
| 75 | 70 | 85 | 73.00 | Predikat B, Lulus |
| 60 | 60 | 80 | 60.00 | Predikat C, Lulus |
| 55 | 50 | 90 | 53.00 | Predikat D, Belum lulus |
| 40 | 30 | 100 | 36.00 | Predikat E, Belum lulus |
| 90 | 90 | 75 | 90.00 | Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran |
| 105 | 80 | 90 | - | Pesan penolakan rentang nilai ujian |
| 80 | -5 | 90 | - | Pesan penolakan rentang nilai tugas |
| 80 | 80 | abc | - | Pesan penolakan tipe |

## Refleksi

Satu masukan tidak valid yang paling mudah terlewat adalah input yang bukan angka, seperti `abc` pada data kehadiran, karena dapat menyebabkan error saat program melakukan perhitungan.

Test case yang membantu menemukan kesalahan urutan kondisi adalah saat nilai kehadiran kurang dari 80%, karena nilai akhir tetap dapat dihitung tetapi status kelulusan harus menyatakan tidak memenuhi syarat kehadiran.
