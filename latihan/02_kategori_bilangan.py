x = int (input("Masukkan bilangan bulat: "))

if x < 0:
    print ("Bilangan negatif")
elif x == 0:
    print ("Bilangan nol")
elif x % 2 == 0:
    print ("Bilangan genap positif")
else:
    print ("Bilangan ganjil positif")